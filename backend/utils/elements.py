class Header:
    SEARCH_INPUT = '/html/body/div[1]/div[1]/form/fieldset/input[1]'


class AssetsPage:
    TICKET = '/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/span'
    SUBSECTOR = '/html/body/div[1]/div[2]/table[1]/tbody/tr[5]/td[2]/span/a'
    STOCK_DIV_YIELD = (
        '/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[4]/span'
    )
    P_L = '/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[4]/span'
    STOCK_P_VP = '/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[4]/span'
    EBITDA = '/html/body/div[1]/div[2]/table[3]/tbody/tr[10]/td[4]/span'
    ROE = '/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[6]/span'
    ROIC = '/html/body/div[1]/div[2]/table[3]/tbody/tr[8]/td[6]/span'
    MIN_PRICE = '/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[4]/span'
    MAX_PRICE = '/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[4]/span'
    PRICE = '/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[4]/span'
    # FIIs
    SEGMENT = '/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[2]/span/a'
    FII_DIV_YIELD = '/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[4]/span'
    FII_P_VP = '/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[4]/span'
    # To get asset type
    SEGMENT_OR_SUBSECTOR_LABEL = (
        '/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[1]/span[2]'
    )
