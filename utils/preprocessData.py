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



def preprocess_bond_data(df):
    # Load the bond data into a Pandas DataFrame
   
    # Convert the issuance_date and maturity_date columns to datetime format
    df['issuance_date'] = formatDateCols(df['issuance_date'])
    df['maturity_date'] = formatDateCols(df['maturity_date'])

    # Remove commas from the coupon_rate column and convert it to a float
    df['coupon_rate'] = couponRate(df['coupon_rate'])


    # Convert the issuance_volume and outstanding_volume columns to numeric format
    df['issuance_volume'] = formatMarketValue(df['issuance_volume'])

    df['duration'] = (df['maturity_date'] - df['issuance_date']).dt.days / 365

    # Rename the columns to remove any spaces
    df.columns = df.columns.str.replace(' ', '_')


    return df