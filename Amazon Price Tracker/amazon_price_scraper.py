from bs4 import BeautifulSoup
import requests
import lxml


class AmazonPriceScraper(object):
    """
    Class to scrape the price of any amazon item.

    Parameters
    ----------
    user_agent : `str`
        Client's user agent string for requests.
    accept_language : `str`
        Acceptable languages for requests.
    currency : `str`
        The currency symbol that price will be in. E.g. '£' or '$'.
    """

    def __init__(self, user_agent, accept_language, currency):
        self.user_agent = user_agent
        self.accept_language = accept_language
        self.currency = currency

    def _get_soup(self, url):
        """
        Uses a url to create a BeautifulSoup object from Amazon.com.

        Parameters
        ----------
        ur : `str`
            The url endpoint to parse.

        Returns
        -------
        `BeautifulSoup Object`
            The html soup that can be parsed for a list of songs.
        """
        response = requests.get(url, headers={"User-Agent": self.user_agent, "Accept-Language": self.accept_language})
        return BeautifulSoup(response.text, 'lxml')

    def get_price(self, url):
        """
        Parses the Amazon.com page for the price of the item.

        Parameters
        ----------
        url : `str`
            The url endpoint to parse.

        Returns
        -------
        `float`
            The price of the item.

        """
        soup = self._get_soup(url)
        price_str_span = soup.find("span", id="priceblock_ourprice").getText()

        # Assume price is in self.currency and not some weird GBP or USD type thing
        price = -1
        try:
            price_str = price_str_span.split(self.currency)[1:]
            price = float(price_str[0])
        except IndexError as ie:
            print(ie)
            print(f"Amazon URL does not contain {self.currency}.")

        return price
