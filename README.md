# 🛒 Ammara Store – E-commerce Web Application

**Ammara Store** is a simple yet functional e-commerce web application built using Django for the backend and HTML, CSS, and Bootstrap for the frontend. It provides a user-friendly interface for customers to browse products, view details, add to cart, and place orders.

---

## 📌 Description

This project simulates the core functionalities of a real-world e-commerce website. It includes features such as product listing, user authentication, cart management, and a checkout system. The platform is responsive, styled with Bootstrap, and includes a visually appealing homepage with product images and categories.

---

## 🛠️ Tech Stack

### 🚀 Frontend
- HTML5  
- CSS3  
- Bootstrap 5  
- JavaScript (for dynamic behavior)

### 🧠 Backend
- Python  
- Django Web Framework  
- SQLite (Default Django database)

---

## 📁 Project Structure

ecommerce-store/
│
├── ecommerce/ # Project-level settings and configurations
│ ├── settings.py
│ └── urls.py
│
├── store/ # Main application
│ ├── models.py # Product, Cart, Order models
│ ├── views.py # Core view logic
│ ├── urls.py # URL patterns
│ └── templates/ # HTML templates (home, product, cart, etc.)
│ └── store/
│ ├── home.html
│ ├── product_detail.html
│ ├── cart.html
│ ├── checkout.html
│
├── static/ # Static files (CSS, JS, images)
│ └── css/
│ └── style.css
│
├── db.sqlite3 # SQLite database file
├── manage.py # Django management script
└── requirements.txt # Python package dependencies


---

## ✨ Features

- 🏠 **Homepage** with background image and product cards  
- 🛍️ **Product Detail View** with image, description, and price  
- 🛒 **Shopping Cart** functionality with quantity update  
- ✅ **User Registration/Login/Logout** system  
- 💳 **Checkout page** for finalizing purchases  
- 🔐 Protected views: only logged-in users can access cart and checkout  
- 🧑‍💼 **Admin Panel** to manage products and orders  
- 🎨 Styled with a formal and aesthetic theme

---

## 🌐 API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | `/`                   | Homepage with products         |
| GET    | `/product/<id>/`      | Product detail page            |
| POST   | `/add-to-cart/`       | Add product to cart            |
| GET    | `/cart/`              | View items in cart             |
| GET/POST | `/checkout/`        | Checkout and order placement   |
| GET    | `/login/`             | Login page                     |
| GET    | `/register/`          | User registration              |
| GET    | `/logout/`            | Logout                         |

---

## ⚙️ Local Setup Instructions
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Visit the application
Open http://127.0.0.1:8000 in your browser.

📜 License
This project is licensed under the MIT License.

