# Spotify Time Machine

## Overview
A Python application that creates Spotify playlists based on Billboard Hot 100 songs from any date in history. Perfect for nostalgic music discovery and playlist creation.

## Features
- Billboard Hot 100 web scraping
- Spotify playlist creation
- Historical music data retrieval
- Automated song search
- Playlist customization
- Date-based song selection

## Technologies Used
- Python
- Spotipy (Spotify API wrapper)
- Beautiful Soup 4
- Requests library
- python-dotenv

## Setup
1. Install required packages:
   ```bash
   pip install spotipy beautifulsoup4 requests python-dotenv
   ```
2. Configure Spotify API credentials in `.env`:
   ```
   client_id=your_spotify_client_id
   client_secret=your_spotify_client_secret
   token=your_spotify_token
   ```
3. Set up Spotify Developer account

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter a date (YYYY-MM-DD)
3. Wait for playlist creation
4. Enjoy your time machine playlist!

## How It Works
1. Scrapes Billboard Hot 100 for specified date
2. Searches songs on Spotify
3. Creates new playlist
4. Adds found songs to playlist

## Note
Requires Spotify Premium account for full functionality
