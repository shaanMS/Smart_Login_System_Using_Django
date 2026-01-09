from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from .models import UserProfile
from .forms import EmailSignupForm, SetPasswordForm, PersonalDetailsForm


from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/h', method='GET', block=True)  # bahut important
def email_signup(request):
    if request.method == 'POST':
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            user = User.objects.create(
                username=email,
                email=email,
                is_active=False
            )

            profile = user.userprofile  # auto-created via signal

            verify_link = f"http://localhost:8000/verify-email/{profile.verification_token}/"

            send_mail(
                'Verify your email',
                f'Click this link to verify:\n{verify_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )

            return render(request, 'email_sent.html')
    else:
        form = EmailSignupForm()

    return render(request, 'email_signup.html', {'form': form})







@ratelimit(key='ip', rate='5/h', method='GET', block=True)  # bahut important
def verify_email(request, token):
    profile = get_object_or_404(UserProfile, verification_token=token)

    profile.email_verified = True
    profile.save()

    request.session['verified_user_id'] = profile.user.id

    return redirect('set_password')








@ratelimit(key='ip', rate='5/h', method='GET', block=True)  # bahut important
def set_password(request):
    user_id = request.session.get('verified_user_id')
    if not user_id:
        return redirect('email_signup')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()

            return redirect('personal_details')
    else:
        form = SetPasswordForm()

    return render(request, 'set_password.html', {'form': form})











def personal_details(request):
    user_id = request.session.get('verified_user_id')
    user = User.objects.get(id=user_id)
    profile = user.userprofile

    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            profile.dob = form.cleaned_data['dob']
            profile.aadhaar = form.cleaned_data['aadhaar']
            profile.city = form.cleaned_data['city']
            profile.state = form.cleaned_data['state']
            profile.address = form.cleaned_data['address']
            profile.save()

            return redirect('/dashboard/')  # 👈 wherever you want
    else:
        form = PersonalDetailsForm()

    return render(request, 'personal_details.html', {'form': form})










from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import LoginForm
from .models import UserProfile
from django.conf import settings



@ratelimit(key='ip', rate='5/h', method='GET', block=True)  # bahut important
# LOGIN VIEW
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/dashboard/")
                else:
                    return render(request, "login.html", {"form": form, "error": "Account inactive. Verify your email first."})
            else:
                return render(request, "login.html", {"form": form, "error": "Invalid credentials"})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# DASHBOARD VIEW (protected)
@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "dashboard.html")


# LOGOUT VIEW
@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return redirect("/login/")


# RESEND VERIFICATION LINK
@ratelimit(key='ip', rate='5/h', method='GET', block=True)  # bahut important
def resend_verification(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            # Try to get profile, create if doesn't exist
            profile, created = UserProfile.objects.get_or_create(user=user)

            if profile.email_verified:
                return render(request, "resend_verification.html", {"message": "Email already verified"})
            else:
                link = f"http://localhost:8000/verify-email/{profile.verification_token}/"
                send_mail(
                    "Verify your email - Resend",
                    f"Click this link:\n{link}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email]
                )
                return render(request, "resend_verification.html", {"message": "Verification link sent"})
        except User.DoesNotExist:
            return render(request, "resend_verification.html", {"message": "Email not registered"})
    return render(request, "resend_verification.html")
