import assets


def get_assets_results(list_of_assets: list) -> list:
    scrape = assets.AssetsScraper(list_of_assets)
    return scrape.results
