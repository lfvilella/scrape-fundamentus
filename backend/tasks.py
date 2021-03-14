""" Tasks.py

This module is responsible to interact with scraper solutions.
"""

from . import assets


def get_assets_results(list_of_assets: list) -> tuple:
    """Get Assets Results

    Args:
        list_of_assets (list): list of assets,
          for example: ['TICKET1', 'TICKET2'].

    Returns:
        list: list of dicts
          [
            {
                'ticket': 'ABCD1',
                'subsector': 'SUBSECTOR',
                'div_yield': '1,1%',
                'p_l': '11,11',
                'p_vp': '1,1',
                'ebitda': '11,11,
                'roe': '11%',
                'roic': '1,0%',
                'min_price': '0,00',
                'max_price': '0,00',
                'price': '0,00',
            }
          ]
    """

    scrape = assets.AssetsScraper(list_of_assets)
    return scrape.results, scrape.errors
