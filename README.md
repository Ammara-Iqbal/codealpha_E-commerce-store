# 🛍️ Simple E-commerce Store
Welcome to the Simple E-commerce Store project! This repository hosts a basic yet functional e-commerce platform designed to showcase fundamental web development concepts using modern technologies. Users can browse products, add items to a shopping cart, view detailed product information, and process orders, all while managing their user accounts.

# ✨ Features
Our e-commerce store comes packed with essential functionalities to provide a smooth shopping experience:

Product Listings: 📦 A beautifully laid out catalog displaying all available products.

Product Details Page: 🔍 Dedicated pages for each product, offering in-depth descriptions, images, and pricing.

Shopping Cart: 🛒 An intuitive cart system allowing users to add, remove, and update quantities of items before checkout.

Order Processing: 💳 Seamless flow for placing orders and managing transactions.

User Registration/Login: 🔐 Secure user authentication and authorization for personalized experiences.

# 🚀 Tech Stack
This project leverages a robust combination of frontend and backend technologies to deliver a responsive and efficient application.

# Frontend
HTML5: For structuring the web content.

CSS3: For styling and creating a visually appealing user interface.

JavaScript: For interactive elements and dynamic content updates.

# Backend
Django (Python): A high-level Python web framework that encourages rapid development and clean, pragmatic design.

SQLite3: A lightweight, file-based database used for storing product, user, and order data. Perfect for development and small-scale deployments.

# 📁 Project Structure
The project is organized into a clear and logical structure, making it easy to navigate and understand.

ecommerce_store/ ├── ecommerce_store/ # Django project settings, URLs, etc. │ ├── pycache/ │ ├── init.py │ ├── asgi.py │ ├── settings.py # Main project settings │ ├── urls.py # Main URL configurations │ └── wsgi.py ├── env/ # Python Virtual Environment ├── media/ # Directory for user-uploaded media (e.g., product images) ├── static/ # Directory for static files (CSS, JS, images) ├── store/ # Django application for e-commerce logic │ ├── migrations/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py # Database models (Products, Orders, Users) │ ├── tests.py │ ├── views.py # Logic for handling requests and rendering templates │ └── urls.py # App-specific URL configurations ├── db.sqlite3 # SQLite database file └── manage.py # Django's command-line utility for administrative tasks

# 🛠️ Local Setup
python -m venv env .\env\Scripts\activate

Install dependencies: Install all required Python packages using pip. pip install -r requirements.txt Apply database migrations: python manage.py makemigrations python manage.py migrate Create a superuser (optional): This allows you to access the Django admin panel to manage products, users, and orders. python manage.py createsuperuser Follow the prompts to create your admin username, email, and password.

Run the development server: Start the Django development server.

python manage.py runserver

The backend API will be accessible at http://127.0.0.1:8000/.


# 📖 API Documentation (Swagger/OpenAPI)
http://127.0.0.1:8000/docs/
