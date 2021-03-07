# import time

# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

from utils import elements, webdriver


class AssetsScraper:
    def __init__(self, assets: list):
        self.url = 'https://fundamentus.com.br/'

        self.scraper = webdriver.BaseScraper()
        self.driver = self.scraper.driver
        self.results = []

        self.start(assets)

    def start(self, assets):
        self.open_site()

        for ticket in assets:
            self.get_data(ticket)

        self.scraper.close_connection()

    def get_data(self, ticket: str):
        input_search = self.scraper.get_by_xpath(
            xpath=elements.Header.SEARCH_INPUT
        )
        input_search.clear()
        input_search.send_keys(ticket)
        input_search.send_keys(Keys.ENTER)

        _ticket = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.TICKET
        ).text
        _price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.PRICE
        ).text

        data = {'ticket': _ticket, 'price': _price}
        self.results.append(data)

    def open_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
