# Stock Price Tracker

## Overview
A Python application that tracks stock prices in real-time and sends notifications when significant price changes occur. Uses the Alpha Vantage API for stock data and SMTP for email notifications.

## Features
- Real-time stock price monitoring
- Price change notifications
- Custom price alerts
- Email notifications

## Technologies Used
- Python
- Alpha Vantage API
- SMTP
- python-dotenv
- Pandas

## Setup
1. Install dependencies:
   ```bash
   pip install requests pandas python-dotenv
   ```
2. Configure environment variables:
   ```
   ALPHA_VANTAGE_KEY=your_key
   EMAIL=your_email
   PASSWORD=your_app_password
   ```

## Usage
1. Add stock symbols to track
2. Set price thresholds
3. Run the tracker:
   ```bash
   python main.py
   ```

## Implementation Details
- API data fetching
- Price analysis
- Alert system
- Email notifications
- Data persistence
