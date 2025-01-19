# Amazon Price Tracker

## Overview
An automated price tracking tool that monitors Amazon product prices and sends email notifications when prices drop below a specified threshold.

## Features
- Automated Amazon product price monitoring
- Email notifications for price drops
- Beautiful Soup web scraping
- SMTP email integration
- Environment variable support for secure credential storage

## Technologies Used
- Python
- Beautiful Soup
- SMTP Library
- Requests
- python-dotenv

## Setup
1. Install required packages
2. Configure environment variables in `.env`:
   ```
   EMAIL=your_email
   PASSWORD=your_app_password
   ```
3. Add product URLs to track

## Usage
Run the script to start tracking prices:
```bash
python main.py
```

## Note
Ensure compliance with Amazon's terms of service when using web scraping tools.
