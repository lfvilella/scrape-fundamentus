""" Tasks.py

This module is responsible to interact with scraper solutions.
"""

from . import assets, cache


def get_assets_results(list_of_assets: list) -> tuple:
    """Get Assets Results

    Args:
        list_of_assets (list): list of assets, example ['TICKET1', 'TICKET2']

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
        errors: dict
          {
            'TICKET1': 'Ativo não encontrado.',
            'TICKET2': 'Ativo não encontrado.'
          }
    """

    _results, _assets_cached = [], []
    for ticket in list_of_assets:
        item_cached = cache.get_item_cached(ticket.upper())
        if item_cached:
            _results.append(item_cached)
            _assets_cached.append(ticket)

    list_of_assets = list(set(list_of_assets) - set(_assets_cached))
    if not list_of_assets:
        return _results, {}  # results, empty errors

    scrape = assets.AssetsScraper(list_of_assets)
    return (scrape.results + _results), scrape.errors
