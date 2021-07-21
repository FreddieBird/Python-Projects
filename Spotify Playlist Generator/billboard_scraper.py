import requests
from bs4 import BeautifulSoup


class BillboardScraper(object):
    """
    For a given date, will scrape and format the top 100 songs from Billboard.com.

    Parameters
    ----------
    base_url : `str`
        The base url of the website to be searched.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def _get_endpoint(self, date):
        """
        Uses a date to create the endpoint for the correct Billboard Hot 100 web page.

        Parameters
        ----------
        date : `str`
            The date string formatted YYYY-MM-DD to scrape songs from.

        Returns
        -------
        `str`
            The webpage endpoint.
        """
        return self.base_url + date

    def _get_soup(self, endpoint):
        """
        Uses an endpoint to create a BeautifulSoup object from Billboard Hot 100 web page.

        Parameters
        ----------
        endpoint : `str`
            The url endpoint to parse.

        Returns
        -------
        `BeautifulSoup Object`
            The html soup that can be parsed for a list of songs.
        """
        response = requests.get(endpoint)
        return BeautifulSoup(response.text, 'html.parser')

    def __call__(self, date):
        """
        Parses the webpage for list of top 100 songs.

        Parameters
        ----------
        date : `str`
            The date string formatted YYYY-MM-DD to scrape songs from.

        Returns
        -------
        `dict{str}`
            The top 100 songs and the respective artist.

        """
        endpoint = self._get_endpoint(date)
        soup = self._get_soup(endpoint)

        song_names_span = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
        artist_names_span = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary")
        songs = [song.getText() for song in song_names_span]
        artists = [artist.getText() for artist in artist_names_span]

        songs = dict(zip(songs, artists))

        return songs
