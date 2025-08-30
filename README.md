# Django Allauth Google OAuth Integration with Django Templates

This guide describes how to integrate Google OAuth authentication into a Django project using the django-allauth package and customize the login flow with Django templates.

## Prerequisites
- Python and Django installed
- A Google Developer Console project with OAuth credentials (Client ID and Client Secret)
- django-allauth installed (`pip install django-allauth`)

## Setup Google OAuth Credentials
1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project for your app.
3. Under "APIs & Services" > "Credentials", create OAuth Client ID credentials.
   - Application type: Web application
   - Authorized JavaScript origins: e.g., `http://localhost:8000`
   - Authorized redirect URIs: e.g., `http://localhost:8000/accounts/google/login/callback/`
4. Copy the Client ID and Client Secret for later use.

## Django Project Configuration

### Install and configure django-allauth

Add the following to your `INSTALLED_APPS` in `settings.py`:

```bash
INSTALLED_APPS = [
# Django apps...
'django.contrib.sites', # Required for allauth
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.google',
]
```

Set your site ID:
```bash
SITE_ID = 1
```

Add authentication backends:
```bash
AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend',
]
```

Add required templates context processors and middleware if not already present.

### Social account settings

Add your Google OAuth credentials in the Django admin panel under **Social Applications**:
- Provider: Google
- Name: Google OAuth
- Client ID: YOUR_GOOGLE_CLIENT_ID
- Secret Key: YOUR_GOOGLE_CLIENT_SECRET
- Sites: Select your site (e.g., example.com)

### URL Configuration

Include django-allauth URLs in your `urls.py`:

from django.urls import path, include
```bash
urlpatterns = [
# Your URLs here
path('accounts/', include('allauth.urls')),
]
```

## Customize Django Templates

Override the default django-allauth templates by adding templates in your project’s template directory. For example, create `login.html` and add a "Sign in with Google" button that points to the Google login URL:

```bash
<a href="{% provider_login_url 'google' %}">Sign in with Google</a>
```

You can customize other templates as needed by following the django-allauth template override mechanism.

## Running the App

1. Run migrations to create necessary tables:
```bash
python manage.py migrate
```

2. Create a superuser to access the admin:
```bash
python manage.py createsuperuser
```

3. Run the development server:
```bash
python manage.py runserver
```

4. Visit `http://localhost:8000/accounts/login/` and use the Google OAuth login button.

---

This setup enables Google OAuth login through django-allauth with full control over the login templates and flow using Django template overrides.

For detailed documentation, see the django-allauth docs: https://docs.allauth.org/en/latest/providers.html#google