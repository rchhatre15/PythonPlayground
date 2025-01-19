# Rain Alert Application

## Overview
A weather monitoring application that sends SMS alerts when rain is expected in your area, using weather API data and Twilio for notifications.

## Features
- Weather condition monitoring
- Rain prediction alerts
- SMS notifications
- Configurable location
- Daily weather updates
- Customizable alert thresholds

## Technologies Used
- Python
- OpenWeather and Twilio API
- python-dotenv
- Requests library

## Setup
1. Install required packages:
   ```bash
   pip install requests twilio python-dotenv
   ```
2. Configure environment variables in `.env`:
   ```
   WEATHER_API_KEY=your_key
   TWILIO_ACCOUNT_SID=your_sid
   TWILIO_AUTH_TOKEN=your_token
   TWILIO_PHONE_NUMBER=your_number
   TARGET_PHONE_NUMBER=target_number
   ```

## Usage
1. Set your location coordinates
2. Run the script:
   ```bash
   python main.py
   ```
3. Receive SMS alerts when rain is expected

## Weather Data
- Temperature
- Precipitation probability
- Weather conditions
- Hourly forecasts

## Note
Requires active Twilio account and OpenWeather API key
