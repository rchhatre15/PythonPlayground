# Personal Blog Website

## Overview
A dynamic blog website built with Flask, featuring a clean, responsive design and full CRUD functionality for blog posts.

## Features
- Responsive web design
- Blog post creation, reading, updating, and deletion
- Contact form integration
- Clean and modern UI
- Bootstrap styling

## Technologies Used
- Python/Flask
- HTML/CSS
- Bootstrap 5
- SQLite/SQLAlchemy
- WTForms for form handling
- Jinja2 templating

## Setup
1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-wtf
   ```
2. Initialize the database
3. Run the Flask application

## Project Structure
```
blog_website/
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── index.html
│   ├── post.html
│   └── about.html
└── main.py
```

## Running the Application
```bash
python main.py
```
Access the website at `http://localhost:5000`
