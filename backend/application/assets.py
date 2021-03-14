""" Assests.py

This module extedens the BaseScraper from utils/webdriver.py
  and implements all scrape logic from website fundamentus.
"""
import traceback

from selenium.webdriver.common.keys import Keys

from utils import elements, webdriver


class AssetsScraper:
    _URL = 'https://fundamentus.com.br/'

    def __init__(self, assets: list):
        """ Init

        Args:
            assets (list): list of assets, for example: ['TICKET1', 'TICKET2']
        """

        self.scraper = webdriver.BaseScraper()
        self.driver = self.scraper.driver
        self.results = []
        self.errors = []

        self.start(assets)

    def start(self, assets: list):
        self.open_site()

        for ticket in assets:
            self._fill_search_input(ticket)

            try:
                type_ = self._get_asset_type()
                if type_ == 'FII':
                    self.get_fiis_data()
                else:
                    self.get_stock_data()

            except Exception as error:
                traceback.print_tb(error.__traceback__)
                self.errors.append({ticket: 'Ativo não encontrado.'})
                pass

        self.scraper.close_connection()

    def _get_asset_type(self) -> str:
        label = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.SEGMENT_OR_SUBSECTOR_LABEL
        ).text
        if label == 'Segmento':
            return 'FII'

        return 'Stock'

    def _fill_search_input(self, ticket: str):
        input_search = self.scraper.get_by_xpath(
            xpath=elements.Header.SEARCH_INPUT
        )
        input_search.clear()
        input_search.send_keys(ticket.upper())
        input_search.send_keys(Keys.ENTER)

    def get_stock_data(self):
        _ticket = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.TICKET
        ).text
        _subsector = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.SUBSECTOR
        ).text
        _div_yield = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.STOCK_DIV_YIELD
        ).text
        _p_l = self.scraper.get_by_xpath(xpath=elements.AssetsPage.P_L).text
        _p_vp = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.STOCK_P_VP
        ).text
        _ebitda = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.EBITDA
        ).text
        _roe = self.scraper.get_by_xpath(xpath=elements.AssetsPage.ROE).text
        _roic = self.scraper.get_by_xpath(xpath=elements.AssetsPage.ROIC).text
        _min_price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.MIN_PRICE
        ).text
        _max_price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.MAX_PRICE
        ).text
        _price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.PRICE
        ).text

        data = {
            'ticket': _ticket,
            'subsector_or_segment': _subsector,
            'div_yield': _div_yield,
            'p_l': _p_l,
            'p_vp': _p_vp,
            'ebitda': _ebitda,
            'roe': _roe,
            'roic': _roic,
            'min_price': _min_price,
            'max_price': _max_price,
            'price': _price,
        }
        self.results.append(data)

    def get_fiis_data(self):
        _ticket = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.TICKET
        ).text
        _segment = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.SEGMENT
        ).text
        _div_yield = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.FII_DIV_YIELD
        ).text
        _p_vp = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.FII_P_VP
        ).text
        _min_price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.MIN_PRICE
        ).text
        _max_price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.MAX_PRICE
        ).text
        _price = self.scraper.get_by_xpath(
            xpath=elements.AssetsPage.PRICE
        ).text

        data = {
            'ticket': _ticket,
            'subsector_or_segment': _segment,
            'div_yield': _div_yield,
            'p_l': '',
            'p_vp': _p_vp,
            'ebitda': '',
            'roe': '',
            'roic': '',
            'min_price': _min_price,
            'max_price': _max_price,
            'price': _price,
        }
        self.results.append(data)

    def open_site(self):
        self.driver.get(self._URL)
        self.driver.maximize_window()
