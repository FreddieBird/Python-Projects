from billboard_scraper import BillboardScraper
from playlist_maker import PlaylistMaker
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BASE_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = config('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = "https://example.com/"

if __name__ == '__main__':

    # ask user for date input
    date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    print(f"Retrieving Top 100 Billboard songs for date {date}...")
    billboard_scraper = BillboardScraper(BASE_URL)
    songs = billboard_scraper(date)
    print(songs)

    print("Authenticating spotify user...")
    playlist_maker = PlaylistMaker(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    print(f"user_id: {playlist_maker.user_id}")

    print("Searching spotify for songs...")
    song_uris = playlist_maker.search_for_songs(songs)

    print("Creating spotify playlist...")
    playlist_maker.create_playlist(song_uris, date)

    print("DONE!")
