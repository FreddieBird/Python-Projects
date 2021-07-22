from amazon_price_scraper import AmazonPriceScraper

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
ACCEPT_LANGUAGE = "en-GB,en-US;q=0.9,en;q=0.8"
CURRENCY = "£"
ITEM_WISHLIST = {"https://www.amazon.co.uk/dp/B07W4CK8KR?tag=camelcamelcam-21&linkCode=ogi&th=1&psc=1&language=en_GB": 200}

EMAIL_ADDRESS = ""
EMAIL_PASS = ""
SMTP_ADDRESS = ""

if __name__ == '__main__':
    # create scraper and emailer
    amazon_price_scraper = AmazonPriceScraper(USER_AGENT, ACCEPT_LANGUAGE, CURRENCY)
    email_notifier = EmailNotifier(EMAIL_ADDRESS, EMAIL_PASS, SMTP_ADDRESS)

    # loop over wishlist of items
    for item_url in ITEM_WISHLIST:
        # get price of item
        price = amazon_price_scraper.get_price(item_url)
        print(f"Price is currently: {CURRENCY}{price}")

        if price == -1:
            continue
        elif price <= ITEM_WISHLIST[item]:
            # send email notification
            email_notifier.send_email(EMAIL_ADDRESS, f"Subject:Amazon Price Alert!\n\n{message}\n{url}")
