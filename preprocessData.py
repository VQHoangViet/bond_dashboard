from imports import *


def formatMarketValue(marketValue):
    if marketValue is None:
        return None
    else:
        return float(marketValue.replace(',', ''))


def formatDateCols(x):
    if x is None:
        return None
    else:
        return pd.to_datetime(x, format='%d/%m/%Y')



def priceDefault(price):
    if price is None:
        return 100000
    else:
        return price

def formatPrice(price):
    if price is None:
        return None
    else:
        return float(price.replace('.', ''))

def couponRate(couponRate):
    if couponRate is None:
        return None
    else:
        return float(couponRate.replace(',', '.'))    

def yieldRate(yieldRate):
    if yieldRate is None:
        return None
    else:
        return float(yieldRate.replace(',', '.'))
    
# calculate duration, return and yield
def ytm_func(ytm, cash_flows, price):    
    return sum([cf / (1 + ytm) ** (i + 1) for i, cf in enumerate(cash_flows)]) + price

