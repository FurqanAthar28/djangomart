# 🛒 DjangoMart

A full-featured e-commerce web application built with **Django**. DjangoMart allows users to browse products by category, manage a shopping cart, and place orders with full checkout functionality. It includes a secure OTP-based email verification system for user registration.

---

## 🚀 Features

- **User Authentication** — Register, login, logout with session management
- **OTP Email Verification** — New users verify their email via a one-time password before account activation
- **Product Catalogue** — Browse products with category filtering on the homepage
- **Product Detail Pages** — Slug-based SEO-friendly URLs for each product
- **Shopping Cart** — Add, remove, and manage cart items with real-time total calculation
- **Paginated Shop** — Shop page with pagination for product listings
- **Checkout** — Full order placement with shipping details (name, address, city, country, zip)
- **Order Management** — Orders saved to database on checkout, cart cleared after order
- **Contact Form** — Email-based contact form for customer inquiries
- **Responsive UI** — Clean Bootstrap-based frontend with carousel, category sections, and vendor logos

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.13, Django 4.2 |
| Database | SQLite (development) |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Auth | Django built-in + OTP via email |
| Email | Gmail SMTP |
| Slugs | django-autoslug |
| Config | python-decouple (.env) |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/FurqanAthar28/djangomart.git
cd djangomart
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django django-autoslug python-decouple
```

### 4. Create `.env` file
Create a `.env` file in the root directory (same level as `manage.py`):
```
SECRET_KEY=your-secret-key-here
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

> **Note:** Use a Gmail App Password, not your regular Gmail password. Generate one at Google Account → Security → App Passwords.

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```
djangomart/
├── newEcommerce/          # Project settings, URLs, views
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── product_app/           # Product, Cart, Checkout models
│   ├── models.py
│   ├── admin.py
│   └── migrations/
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── shop.html
│   ├── cart.html
│   ├── checkout.html
│   ├── signin.html
│   ├── signup.html
│   └── ...
├── static/                # CSS, JS, images
├── .env                   # Environment variables (not committed)
├── .gitignore
└── manage.py
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `EMAIL_HOST_USER` | Gmail address for sending emails |
| `EMAIL_HOST_PASSWORD` | Gmail app password |

---

## 📸 Screenshots

> Homepage with category filtering and product carousel

> Shop page with paginated product listings

> Cart with quantity management and total price

---

## 👨‍💻 Author

**Furqan Athar**
- GitHub: [@FurqanAthar28](https://github.com/FurqanAthar28)
- LinkedIn: [Furqan Athar](https://www.linkedin.com/in/furqan-athar)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
