# Movie Ranking Website

## Overview
A dynamic web application for ranking and reviewing movies, built with Flask and SQLAlchemy. Features a clean, responsive interface for adding, rating, and reviewing movies.

## Features
- Movie database management
- Rating system
- Movie review functionality
- Responsive design
- Search capabilities
- Sort by rating/title
- Edit and delete functionality

## Technologies Used
- Python/Flask
- HTML/CSS
- WTForms
- SQLAlchemy
- SQLite database

## Project Structure
```
movie_ranking_website/
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── main.py
└── movie.db
```

## Setup & Usage
1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-wtf
   ```
2. Initialize the database
3. Start the server:
   ```bash
   python main.py
   ```
4. Access at `http://localhost:5000`
5. Add movies, rate them, and write reviews

## Database Schema
- Title
- Year
- Description
- Rating
- Ranking
- Review
- Image
