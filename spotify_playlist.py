import requests
from bs4 import BeautifulSoup
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = 'YOUR_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
scope = 'playlist-modify-public'
username = 'YOUR_USERNAME'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               scope=scope))
user_id = sp.current_user()["id"]

date = input('choose a year with the format YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
html_page = response.text
soup = BeautifulSoup(html_page, 'html.parser')
# print(soup.prettify())
first_song = soup.find_all(name='h3', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')
song_names = soup.find_all(name="h3",
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

hit100 = [song.getText().strip() for song in first_song]
for song in song_names:
    hit100.append(str(song.getText().strip()))
print(hit100)

playlist_name = f"HOT100: {date}"

playlist = sp.user_playlist_create(user=username, name=playlist_name)

songs = []
for song_name in hit100:
    result = sp.search(q=song_name)
    songs.append(result['tracks']['items'][0]['uri'])


sp.playlist_add_items(playlist_id=playlist['id'], items=songs)

