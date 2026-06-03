# kcellshopalpha

KCELL Internship Tour Project: Online Shop

A rough draft of an online shop made by using Django, PostgreSQL and Docker Compose to demonstrate skills for the internship.

----

How to run the project:

Requirements:

"Docker Dekstop and Docker Compose installed"

Steps:

Write in terminal:
"bash
git clone https://github.com/a-nurpeissov/kcellshopalpha.git
cd kcellshopalpha
docker compose up --build"

It will:

Start PostgreSQL in the db container
Buind and run Django in the web container
Apply migrations (for models)
Run the development server on 127.0.0.1:8000 (or other depending on your device and OS)

Open any browser and type in the url:
http://127.0.0.1:8000/

Create a superuser for the admin panel:

bash
docker compose exec web python manage.py createsuperuser

You can access admin panel with:
http://127.0.0.1:8000/admin/

-----

Project architecture

The project is made in Django as a Django project with a single main app

File structure:

- kcellshopalpha/ 
  - settings.py – Django settings, database configuration (PostgreSQL in Docker / SQLite locally), installed apps  
  - urls.py – root URL configuration, includes store.urls 
  - wsgi.py, asgi.py – server entry points

- store/ – main shop application  
  - models.py– domain models:
    - Product– product (name, description, price, image URL)
    - Order – order (customer name, phone number, creation time)
    - OrderItem – order line (order reference, product reference, quantity)

  - views.py – views for:
       - product list
       - product detail
       - cart page (reading/updating cart stored in session)
       - checkout page (form with name and phone, creates Order and OrderItems)
       - order success page

  - urls.py – app routes:
    - catalog (/)
    - product detail
    - add to cart
    - cart view
    - checkout
  - templates/store/ – server‑rendered HTML templates (Django Templates):
    - products list page
    - product detail page
    - cart page
    - checkout page
    - order success page


- Docker files  
  - Dockerfile – builds the Django web image (Python 3.12, installs requirements.txt, sets up /app)  
  - docker-compose.yml – defines services:
    - db – PostgreSQL container configured via environment variables
    - web – Django container depending on db, exposing port 8000:8000

---

Data model

 Product

- id (auto, primary key)  
- name 
- description  
- price
- image (URL)

Order

- id (auto, primary key)  
- customer_name
- phone_number
- created_at (timestamp when the order is created)

### OrderItem

- id (auto, primary key)  
- order (foreign key to Order)  
- product (foreign key to Product)  
- quantity

----

Technologies used

Language and framework:
  -Python 3.12
  - Django 6 (server-side rendering with Django Templates)

Database:
  - PostgreSQL (in Docker, main mode)
  - SQLite (optional local development without Docker)

Containerization:
  - Docker
  - Docker Compose

- Frontend:
  - Django Templates (HTML rendered on the server)
  - No React/Vue/Angular, only server-side rendering

- Other:
  - Git and GitHub for version control
  - requirements.txt for Python dependencies

---

Also keep in mind that I used Brew version of Docker, Django and postgresql on MacOS to create this app, the command lines may differ depending on your OS.

