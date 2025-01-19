# Coffee Shop Review Website

## Overview
A Flask-based web application for reviewing and rating coffee shops, featuring a clean interface for adding and viewing cafe information including WiFi availability and power outlet access.

## Features
- Add new cafe entries with detailed information
- View all cafes in a clean, tabulated format
- Rate cafes based on coffee quality, WiFi strength, and power outlet availability
- Location information with Google Maps integration
- CSV data storage for simplicity

## Technologies Used
- Python/Flask
- HTML/CSS
- CSV for data storage

## Setup
1. Install required packages:
   ```bash
   pip install flask flask-wtf flask-bootstrap
   ```
2. Configure the application
3. Initialize the CSV database

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Access the website at `http://localhost:5000` and browse existing entries
3. Add new cafes at `http://localhost:5000/add`

## Data Structure
Stores information about:
- Cafe name
- Location
- Opening/Closing times
- Coffee quality rating
- WiFi strength rating
- Power outlet availability
