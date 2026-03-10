Markdown<div align="center">

  <h1>🛡️ Smart Login System Using Django</h1>

  <p>
    <strong>A secure, production-ready email-verified authentication system with smart multi-step onboarding, rate limiting, and clean UI.</strong>
  </p>

  <!-- Badges row -->
  <p>
    <img src="https://img.shields.io/badge/Django-5.2.5-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django version" />
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Security-Rate%20Limited%20%26%20CSRF%20Protected-brightgreen?style=for-the-badge" alt="Security" />
    <img src="https://img.shields.io/badge/Email%20Verification-Working-success?style=for-the-badge" alt="Email Verification" />
    <img src="https://img.shields.io/badge/UI-Bootstrap--like-blueviolet?style=for-the-badge" alt="UI" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  </p>

  <p>
    <a href="https://github.com/shaanMS/Smart_Login_System_Using_Django/stargazers">
      <img src="https://img.shields.io/github/stars/shaanMS/Smart_Login_System_Using_Django?style=social" alt="GitHub stars" />
    </a>
    <a href="https://github.com/shaanMS/Smart_Login_System_Using_Django/forks">
      <img src="https://img.shields.io/github/forks/shaanMS/Smart_Login_System_Using_Django?style=social" alt="GitHub forks" />
    </a>
    <a href="https://github.com/shaanMS/Smart_Login_System_Using_Django/issues">
      <img src="https://img.shields.io/github/issues/shaanMS/Smart_Login_System_Using_Django?style=social" alt="GitHub issues" />
    </a>
  </p>

  <br />

  <img src="https://via.placeholder.com/800x450/092E20/FFFFFF?text=Dashboard+Preview" alt="Dashboard Preview" width="800" />
  <br><small><em>Modern dashboard after successful login & profile completion</em></small>

</div>

## ✨ Features

- 📧 **Multi-step Smart Signup Flow**  
  Email → Verification Link → Set Password → Complete Profile → Dashboard
- 🔐 **Secure Authentication**  
  - Email verification with unique UUID token  
  - Django’s built-in password hashing & auth  
  - Inactive user blocking until verified
- 🛡️ **Security Best Practices**  
  - Rate limiting on signup, login, verify & resend (django-ratelimit)  
  - Full CSRF protection  
  - HttpOnly session cookies  
  - XSS-safe templates
- 📬 **Email Integration**  
  SMTP backend (configurable for production)  
  Local testing support (e.g. MailHog / localhost:1025)
- 🧑‍💼 **Profile Management**  
  Auto profile creation via Django signals  
  Collects personal details (name, DOB, Aadhaar, address, etc.)
- 📊 **User Dashboard**  
  Shows verification status, join date, quick actions & logout
- 🔄 **Recovery Flows**  
  Resend verification email  
  Clean 403 forbidden / CSRF failure page
- 🎨 **Clean & Responsive UI**  
  Simple, mobile-friendly templates with form validation feedback

## 🖼️ Screenshots

<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/email_signup.png" width="400" alt="Email Signup"/></td>
      <td><img src="screenshots/email_sent.png" width="400" alt="Email Sent"/></td>
    </tr>
    <tr>
      <td><img src="screenshots/set_password.png" width="400" alt="Set Password"/></td>
      <td><img src="screenshots/personal_details.png" width="400" alt="Personal Details"/></td>
    </tr>
    <tr>
      <td><img src="screenshots/login.png" width="400" alt="Login"/></td>
      <td><img src="screenshots/dashboard.png" width="400" alt="Dashboard"/></td>
    </tr>
    <tr>
      <td><img src="screenshots/resend_verification.png" width="400" alt="Resend Verification"/></td>
      <td><img src="screenshots/403.png" width="400" alt="403 Access Denied"/></td>
    </tr>
  </table>
</div>

> *Tip: Place real screenshots in a `screenshots/` folder and update paths above.*

## 🚀 Tech Stack

- **Backend:** Django 5.2.5
- **Database:** SQLite (dev) – easily switch to PostgreSQL/MySQL
- **Email:** SMTP (localhost:1025 for testing)
- **Security:** django-ratelimit, CSRF middleware, HttpOnly cookies
- **Frontend:** HTML + CSS (Bootstrap-inspired styling)
- **Other:** Django signals, custom forms, UUID tokens

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/shaanMS/Smart_Login_System_Using_Django.git
cd Smart_Login_System_Using_Django

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt    # (create this file if missing)

# 4. Apply migrations
python manage.py migrate

# 5. (Optional) Create superuser
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver

# 7. (For email testing) Run MailHog or similar in another terminal
#    http://localhost:8025 to view sent emails
Open → http://127.0.0.1:8000/
🛠️ Setup for Production (Important!)

Change SECRET_KEY (use environment variable!)
Set DEBUG = False
Configure real SMTP (Gmail, SendGrid, Amazon SES…)
Add ALLOWED_HOSTS
Enable HTTPS → uncomment SECURE_* settings
Use PostgreSQL instead of SQLite
Consider Celery + Redis for async email sending

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
💡 Why this project?
Great for:

Understanding Django custom authentication flows
Learning email verification patterns
Practicing security middlewares & rate limiting
Preparing for interviews (auth, forms, signals, security)

Feel free to ⭐ the repo if you find it useful!


# Email Verification Project Screenshots

### Login Page
![Login Secure Access](screenshots/LoginSecureAccess.png)

### Dashboard
![Dashboard User Portal](screenshots/DashboardUserPortal.png)

### Email Sent Confirmation
![Email Sent Check Your Inbox](screenshots/EmailSentCheckYourInbox.png)

### Resend Verification
![Resend Verification Account Access](screenshots/ResendVerificationAccountAccess.png)

### Mail Preview
![Mail](screenshots/Mail.png)

### Access Denied Page
![Access Denied](screenshots/AccessDenied.png)
