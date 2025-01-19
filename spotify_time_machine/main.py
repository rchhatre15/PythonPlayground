import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
token = os.getenv("token")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/?code=AQD0b9uZ4VNjoUW-JpnmOS0vUUkEwAsGHs5_qHickA9zxIBiyg3Ax2bLyfW1-1CWFyJKL8FcvlUolClqoLsZHrF4zC84sI3bxmPlnhC5sDI0HEvEpmZiveBdYFeNxXiTvLyE21oMIrIg3llKb69PEzv1FrdlYmngANREv5yhJHFoCzYi0rtM6z6rAKbg3lM",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path=".cache",
        username="rchhatre15", 
    )
)
user_id = sp.current_user()["id"]
#print(user_id)

time = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}", headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
soup.prettify()
# titles = soup.find_all(name="h3", id="title-of-a-story")
# song_names = [title.getText().strip() for title in titles if title.getText().strip() not in ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', 'Gains in Weekly Performance', 'Additional Awards']][:100]
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
#print(song_names)

URI_list = []
for song in song_names:
    try:
        # artist_info = requests.get(
        # 'https://api.spotify.com/v1/search',
        # headers={
        #     'Authorization': 'Bearer {token}'.format(token=token)
        # },
        # params={ 'q': {song}, 'type': 'track', 'year': {time[0:4]} })
        # URI_list.append(artist_info.json()["tracks"]["items"][0]["uri"])
        URI_list.append(sp.search(q=f"track:{song} year:{time[0:4]}", type="track", limit=1)["tracks"]["items"][0]["uri"])
    except:
        print(f"{song} not found")

# print(URI_list)
playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=URI_list)
