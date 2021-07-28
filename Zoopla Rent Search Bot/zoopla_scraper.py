from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import re


class ZooplaScraper(object):
    """
    A class that scrapes all the rent prices, links and addresses
    for given filters.

    Parameters
    ----------
    filters : dict{str:str}
        The filters to input into Zoopla search bar.
    chrome_driver_path : `str`
        The path to your locally stored chrome driver.
    """
    base_url = "https://www.zoopla.co.uk"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    ACCEPT_LANGUAGE = "en-GB,en-US;q=0.9,en;q=0.8"

    def __init__(self, filters, chrome_driver_path):
        self.area = filters['area']
        self.min_bedrooms = filters['min_bedrooms']
        self.max_bedrooms = filters['max_bedrooms']
        self.min_pcm = filters['min_pcm']
        self.max_pcm = filters['max_pcm']
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(ZooplaScraper.base_url)

        time.sleep(5)

        url = self.__enter_filters()
        response = requests.get(url, headers={"User-Agent": ZooplaScraper.USER_AGENT, "Accept-Language": ZooplaScraper.ACCEPT_LANGUAGE})
        self.soup = BeautifulSoup(response.text, 'lxml')

    def __enter_filters(self):
        """
        Uses Selenium to fill in the query bar using the given filters.
        """
        # click accept cookies
        try:
            iframe = self.driver.find_element_by_xpath('//*[@id="gdpr-consent-notice"]')
            self.driver.switch_to.frame(iframe)
            self.driver.find_element_by_xpath('//*[@id="save"]/span[1]/div/span').click()
            time.sleep(1)
            self.driver.switch_to.default_content()
        except NoSuchElementException as e:
            print(e)

        # get all dropdown options
        options = self.driver.find_elements_by_tag_name("option")

        # click To Rent
        self.driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[3]/div[1]/a[2]').click()

        # location
        area = self.driver.find_element_by_xpath('//*[@id="header-location"]')
        area.send_keys(self.area)

        # bedrooms
        self.driver.find_element_by_xpath('//*[@id="AnyBeds_testId"]').click()
        min_bed = Select(self.driver.find_element_by_id('beds_min'))
        min_bed.select_by_visible_text(self.min_bedrooms)

        max_bed = Select(self.driver.find_element_by_id('beds_max'))
        max_bed.select_by_visible_text(self.max_bedrooms)

        time.sleep(1)

        # rent price
        self.driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[3]/div[2]/div/div[5]/div/button').click()
        min_pcm = Select(self.driver.find_element_by_xpath('//*[@id="price_min_monthly"]'))
        min_pcm.select_by_visible_text(self.min_pcm)

        max_pcm = Select(self.driver.find_element_by_xpath('//*[@id="price_max_monthly"]'))
        max_pcm.select_by_visible_text(self.max_pcm)

        # search
        self.driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[3]/div[2]/div/div[8]/button').click()

        url = self.driver.current_url

        # exit driver safely
        # self.driver.quit()

        return url

    def get_links(self):
        """
        Uses BeautifulSoup to scrape zoopla webpage for acommodation links.
        """
        links = [ZooplaScraper.base_url + l['href'] for l in self.soup.find_all("a", href=re.compile("/to-rent/details/[0-9]"))]
        links = [i for n, i in enumerate(links) if i not in links[:n]]
        print(links)
        print(len(links))
        return links

    def get_prices(self):
        """
        Uses BeautifulSoup to scrape zoopla webpage for acommodation prices.
        """
        prices = [p.getText() for p in self.soup.find_all("p", text=re.compile("£"))]
        prices = prices[1:]
        print(prices)
        print(len(prices))
        return prices

    def get_addresses(self):
        """
        Uses BeautifulSoup to scrape zoopla webpage for acommodation addresses.
        """
        addresses = [a.getText() for a in self.soup.find_all("p", text=re.compile(self.area))]
        print(addresses)
        print(len(addresses))
        return addresses
