# Movie Ranking Website

A Flask-based web application that allows users to create and manage their personal movie rankings. The application integrates with The Movie Database (TMDB) API to provide accurate and up-to-date movie information.

## Features
- Movie database management
- Rating and reviewsystem
- Movie review functionality
- Responsive design
- Dynamic sorting by rating
- Edit and delete functionality
- Session-based search results management
- TMDB API Integration for movie search and data
- Seamless card-based UI with movie posters

## Technologies Used
- Python/Flask
- HTML/CSS
- WTForms
- SQLAlchemy
- SQLite database
- Flask-SQLAlchemy for database ORM
- Flask-WTF for form handling and CSRF protection
- SQLite database
- TMDB API for movie data

## Project Structure
```
movie_ranking_website/
├── instance/
│   ├── movies.db
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── main.py
├── requirements.txt```

## Setup & Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
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
- Review
- Image
