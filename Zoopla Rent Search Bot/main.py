from zoopla_scraper import ZooplaScraper
from form_filler import FormFiller

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
FILTERS = {
    'area': 'NW1',
    'min_bedrooms': 'No min',
    'max_bedrooms': '2',
    'min_pcm': 'No min',
    'max_pcm': '£1,500 pcm'
}
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSelZfO8RZ6SsLRuAsXgd89ufBdrh7p5Yeg_NqE8UDZLKeVcFg/viewform"


if __name__ == '__main__':
    # scrape data from zoopla
    scraper = ZooplaScraper(FILTERS, CHROME_DRIVER_PATH)
    links = scraper.get_links()
    prices = scraper.get_prices()
    addresses = scraper.get_addresses()

    # fill in google form and sheet
    form_filler = FormFiller(FORM_LINK, CHROME_DRIVER_PATH, links, prices, addresses)
    form_filler.fill_forms()
