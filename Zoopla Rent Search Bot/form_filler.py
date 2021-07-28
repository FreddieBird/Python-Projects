from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


class FormFiller(object):
    """
    A class that fills in google forms.

    Parameters
    ----------
    form_link : `str`
        URL of the google form.
    chrome_driver_path :   `str`
        The path to your locally stored chrome driver.
    links : `list[str]`
        Acommodation URLs.
    prices : `list[str]`
        Acommodation prices.
    addresses : `list[str]`
        Acommodation addresses.
    """

    def __init__(self, form_link, chrome_driver_path, links, prices, addresses):
        self.links = links
        self.prices = prices
        self.addresses = addresses
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(form_link)

        time.sleep(5)

    def fill_forms(self):
        """
        Loops through each acommodation and fills in a google form.
        """

        for i in range(len(self.links)):
            # address
            ans = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            ans.send_keys(self.addresses[i])

            # price
            ans = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            ans.send_keys(self.prices[i])

            # links
            ans = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            ans.send_keys(self.links[i])

            # submit
            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

            time.sleep(1)
            # submit another form
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            time.sleep(3)
