# 🛒 DjangoMart

A full-featured e-commerce web application built with Django. Features OTP email verification, product catalogue with category filtering, shopping cart, paginated shop, and full checkout with order management.

## ✨ Features

- User Authentication with OTP email verification
- Product catalogue with category filtering
- SEO-friendly slug-based product URLs
- Shopping cart with quantity management and real-time total
- Paginated shop page
- Full checkout with order saving
- Contact form via email
- Responsive Bootstrap UI

## 🛠️ Tech Stack

- Python 3.13 / Django 4.2
- SQLite (development)
- Bootstrap / HTML / CSS / JavaScript
- Gmail SMTP for emails
- django-autoslug
- python-decouple (.env)

## ⚙️ Setup

1. Clone the repo
   git clone https://github.com/FurqanAthar28/djangomart.git
   cd djangomart

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install django django-autoslug python-decouple

4. Create .env file in root
   SECRET_KEY=your-secret-key
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password

5. Run migrations
   python manage.py migrate

6. Start server
   python manage.py runserver

Visit http://127.0.0.1:8000

## 👨‍💻 Author

Furqan Athar
- GitHub: https://github.com/FurqanAthar28
- LinkedIn: https://www.linkedin.com/in/furqan-athar
