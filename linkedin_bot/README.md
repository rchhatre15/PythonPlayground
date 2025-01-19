# LinkedIn Job Application Bot

## Overview
An automated bot built with Selenium WebDriver that streamlines the job application process on LinkedIn. This bot automatically logs into LinkedIn, navigates to job listings, and helps manage the application process.

## Features
- Automated LinkedIn login with secure credential management
- Job search navigation and filtering
- Easy application process automation (almost :-))
- Environment variable support for secure credential storage
- Chrome WebDriver integration with custom options

## Technologies Used
- Python
- Selenium WebDriver
- python-dotenv for environment management
- Chrome WebDriver

## Setup
1. Install required packages:
   ```bash
   pip install selenium python-dotenv
   ```
2. Create a `.env` file with your LinkedIn credentials:
   ```
   LINKEDIN_EMAIL=your_email
   LINKEDIN_PASSWORD=your_password
   ```
3. Ensure Chrome WebDriver is installed and in your PATH

## Usage
1. Set up your environment variables in `.env`
2. Run the script:
   ```bash
   python main.py
   ```
3. The bot will automatically:
   - Log into LinkedIn
   - Navigate to the specified job search URL
   - Process job listings

## Security Notes
- Credentials are stored securely in `.env` file
- Uses environment variables for sensitive information
- `.env` file is included in `.gitignore`

## Disclaimer
This bot is for educational purposes only. Please review LinkedIn's terms of service before using automated tools.
