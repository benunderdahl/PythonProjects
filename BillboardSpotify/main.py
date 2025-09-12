from bs4 import BeautifulSoup
import os
import requests
from spotipy.oauth2 import SpotifyOAuth

BB_ENDPOINT = "https://billboard.com/charts/hot-100/"
spotify_client = os.getenv("SPOTIFY_CLIENT")
spotify_secret = os.getenv("SPOTIFY_SECRET")
date = input("Enter a date in YYYY-MM-DD format: ")

response = requests.get(url=f"{BB_ENDPOINT}/{date}", headers = header)
soup = BeautifulSoup(response.text, "html.parser")

titles = [title.get_text().strip() for title in soup.select("li ul li h3")]
artists = [artist.get_text().strip() for artist in soup.select("li ul li span.c-label.a-no-trucate")]

print(titles)
print(artists)