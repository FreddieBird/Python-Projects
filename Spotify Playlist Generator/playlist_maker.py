import spotipy
from spotipy.oauth2 import SpotifyOAuth


class PlaylistMaker(object):
    """
    Connects to Spotify API to create a playlist.

    Parameters
    ----------
    client_id : `str`
        Client ID.
    client_secret : `str`
        Client Secret ID.
    redirect_uri : `str`
        The redirect uri.
    """

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=self.redirect_uri,
                client_id=self.client_id,
                client_secret=self.client_secret,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def search_for_songs(self, songs):
        """
        Uses spotipy library to search for a song and then stores its uri.

        Parameters
        ----------
        songs : `dict{str: str}`

        Returns
        -------
        `list[str]`
            Song URIs.
        """
        song_uris = []
        for song in songs:
            result = self.sp.search(q=f"track:{song} artist:{songs[song]}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                print("Adding song: {result["tracks"]["items"][0]["name"]}")
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        return song_uris

    def create_playlist(self, song_uris, date):
        """
        Creates playlist and adds songs to it.

        Parameters
        ----------
        song_uris : `list[str]`
            List of song_uris to add to playlist.
        date : `str`
            The date of songs searched for.
        """
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{date} Billboard 100", public=False)
        print(playlist)

        print("Adding songs to playlist...")
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
