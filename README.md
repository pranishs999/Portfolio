# Pranish Shrestha — Portfolio (Django + Tailwind)

A personal portfolio website built with **Django**, **Tailwind CSS** (via CDN), vanilla **JavaScript**, and **SMTP** email notifications on the contact form. Includes a login-protected dashboard to manage portfolio content dynamically.

## Features

- **Responsive Portfolio** — Hero, About, Skills, Experience, Achievements, Projects, and Contact sections
- **Dynamic Content** — Experience, Training/Certifications, and Achievements are stored in the database and rendered dynamically
- **Admin Dashboard** — Login-protected page at `/dashboard/` to add and delete Experience, Training, and Achievement entries
- **Contact Form with Email** — Visitors can send messages via the contact form; you get an email notification through Django's SMTP
- **Template Inheritance** — `base.html` handles the shared layout (nav, footer, scripts); `home.html` extends it for page content

## Quick Start

```bash
# 1. Create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy env template and fill in your credentials
cp .env.example .env
# Edit .env with your SMTP Email credentials (e.g. Gmail App Password)

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for dashboard access)
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Open http://127.0.0.1:8000

## Dashboard

The dashboard is available at `/dashboard/` and requires authentication.

1. Navigate to `http://127.0.0.1:8000/dashboard/`
2. You'll be redirected to the login page
3. Sign in with your superuser credentials
4. From the dashboard you can:
   - **Add** new Experience, Training, or Achievement entries
   - **Delete** existing entries (hover over an entry to reveal the delete button)
5. Changes appear immediately on the homepage

## Email Setup

1. Create a Gmail account (or use your existing one).
2. Go to your Google Account > Security > 2-Step Verification and enable it.
3. Generate an "App Password".
4. Put the credentials in `.env`:
   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=pranishs999@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password_here
   ```

When someone submits the contact form, you'll get an email sent to `EMAIL_HOST_USER` with their name, email, subject, and message.

If email credentials are missing or incorrect, the form will return an error status 500 but still validate properly.

## Project Structure

```
portfolio_django/
├── manage.py
├── requirements.txt
├── .env.example
├── db.sqlite3
├── portfolio_project/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main/                           # Portfolio app
    ├── models.py                   # Experience, Training, Achievement models
    ├── views.py                    # Home, Dashboard, Logout, Contact views
    ├── urls.py                     # Routes for home, dashboard, login, logout
    ├── forms.py                    # ModelForms + ContactForm
    ├── admin.py                    # Admin registration for all models
    ├── templates/
    │   ├── main/
    │   │   ├── base.html           # Shared layout (nav, footer, scripts)
    │   │   ├── home.html           # Homepage (extends base.html)
    │   │   └── dashboard.html      # Login-protected dashboard
    │   └── registration/
    │       └── login.html          # Custom login page
    └── static/main/
        ├── css/style.css
        └── js/main.js
```

## Models

| Model | Fields |
|---|---|
| **Experience** | `role`, `org`, `period`, `current` (bool), `desc` |
| **Training** | `title`, `issuer` |
| **Achievement** | `name`, `year`, `result` |

## Tech Stack

- **Backend**: Django 5.x, Python 3
- **Frontend**: Tailwind CSS (CDN), vanilla JS
- **Database**: SQLite (default)
- **SMS**: SMTP Email (Django built-in)
- **Auth**: Django built-in authentication

## Deploy

The project uses SQLite by default and is ready for any host that runs Django (Render, Railway, Fly.io, PythonAnywhere). For production:
- Set `DEBUG=False` in `.env`
- Add your domain to `ALLOWED_HOSTS`
- Run `python manage.py collectstatic`
- Use Gunicorn or similar: `gunicorn portfolio_project.wsgi`
