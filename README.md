# 🛒 DjangoMart

A modern E-commerce web application built with Django that allows users to browse products, manage their cart, and place orders through a clean and responsive interface.

> This project was developed as part of my Django learning journey and demonstrates core web development concepts including authentication, CRUD operations, session management, and deployment.

---

## 🌐 Live Demo

**Website:** https://furqan.pythonanywhere.com

---



## 📸 Screenshots

### Home Page

![Home](images/home.png)

### Shop Page

![Shop](images/shop.png)

### Product Details

![Product Details](images/product-details.png)

### Shopping Cart

![Cart](images/cart.png)

### Checkout

![Checkout](images/checkout.png)

### Login

![Login](images/login.png)

### Register

![Register](images/register.png)



## ✨ Features

- User Registration & Login
- Product Catalog
- Product Details
- Shopping Cart
- Checkout System
- Django Admin Dashboard
- Email Configuration
- Static File Management
- Responsive UI
- Secure Environment Variables (.env)
- Production Deployment

---

## 🛠 Tech Stack

### Backend

- Python 3
- Django 6

### Database

- SQLite

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

### Deployment

- PythonAnywhere
- WhiteNoise

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
DjangoMart
│
├── newEcommerce/
├── product_app/
├── templates/
├── static/
├── staticfiles/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/FurqanAthar28/djangomart.git
```

Move into the project

```bash
cd djangomart
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create your local environment file from the example:

```bash
copy .env.example .env
```

Generate a unique Django secret key and set it as `SECRET_KEY` in `.env`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Keep `.env` private and out of version control. For deployment, set `DEBUG=False`,
configure `ALLOWED_HOSTS` for your domain, and provide email credentials through
environment variables rather than committing them.

Run migrations

```bash
python manage.py migrate
```

Run development server

```bash
python manage.py runserver
```

## 🧪 Tests and Lint

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run Django checks, the test suite, and Ruff:

```bash
python manage.py check
python manage.py test
python -m ruff check .
```

GitHub Actions runs these checks for pushes and pull requests.

---

## 🚀 Deployment

The application is deployed on **PythonAnywhere**.

### PythonAnywhere with PostgreSQL

Create a PostgreSQL database from the PythonAnywhere **Databases** tab and note
the PostgreSQL server host and port, database name, username, and password.
PythonAnywhere-hosted PostgreSQL requires a paid account with PostgreSQL enabled.
Use the values shown in the **Databases** tab rather than the example below.

In a Bash console, install the PostgreSQL production dependencies and migrate the
new database:

```bash
pip install -r requirements-postgres.txt
cp .env.example .env
```

Edit `.env` on the server and set `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`,
`CSRF_TRUSTED_ORIGINS`, and `DATABASE_URL`:

```dotenv
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DATABASE
DATABASE_SSL_REQUIRE=False
```

Once HTTPS is working, also set `SESSION_COOKIE_SECURE=True`,
`CSRF_COOKIE_SECURE=True`, and `SECURE_SSL_REDIRECT=True`. Run
`python manage.py check --deploy` with the production environment before reloading
the web app.

Use the exact connection details from PythonAnywhere and URL-encode any special
characters in the database username, password, or database name. Set
`DATABASE_SSL_REQUIRE=True` only if your database provider requires SSL. Keep
`.env` private and never commit it. The app uses SQLite when `DATABASE_URL` is
unset, so local development remains unchanged.

The new PostgreSQL database starts empty; this setup does not copy data from
`db.sqlite3`. Apply migrations and collect static files:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

In the PythonAnywhere **Web** tab, configure a manual Django web app to use the
project's virtualenv and WSGI file, set the project directory and static files
mapping if needed, then reload the web app after deployment or configuration
changes.

For local PostgreSQL testing and development dependencies, install
`requirements-dev.txt`; GitHub Actions runs the test suite against PostgreSQL.

---

## 📚 What I Learned

During this project I learned:

- Django Models
- Django ORM
- URL Routing
- Template Engine
- Forms
- Authentication
- Sessions
- CRUD Operations
- Static & Media Files
- Django Admin
- Git & GitHub
- Production Deployment
- Environment Variables
- WhiteNoise Configuration

---

## 🔮 Future Improvements

- Product Search
- Product Categories
- Wishlist
- Order History
- Payment Gateway
- Product Reviews
- PostgreSQL
- Docker
- REST API
- JWT Authentication

---

## 👨‍💻 Author

**Furqan Athar**

GitHub:
https://github.com/FurqanAthar28

---

⭐ If you found this project helpful, consider giving it a star.
