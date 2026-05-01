# DjangoMart

A full-featured e-commerce web application built with Django. Features OTP email verification, product catalogue with category filtering, shopping cart, paginated shop, and full checkout with order management.

## Features

- User Authentication with OTP email verification
- Product catalogue with category filtering
- SEO-friendly slug-based product URLs
- Shopping cart with quantity management
- Paginated shop page
- Full checkout with order saving
- Contact form via email
- Responsive Bootstrap UI

## Tech Stack

- Python 3.13 / Django 4.2
- SQLite (development)
- Bootstrap / HTML / CSS / JavaScript
- Gmail SMTP for emails
- django-autoslug
- python-decouple

## Setup

\\\ash
git clone https://github.com/FurqanAthar28/djangomart.git
cd djangomart
python -m venv venv
venv\Scripts\activate
pip install django django-autoslug python-decouple
\\\`n
Create a .env file:
\\\`nSECRET_KEY=your-secret-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
\\\`n
Then run:
\\\ash
python manage.py migrate
python manage.py runserver
\\\`n
## Author

**Furqan Athar**
- GitHub: https://github.com/FurqanAthar28
- LinkedIn: https://www.linkedin.com/in/furqan-athar
