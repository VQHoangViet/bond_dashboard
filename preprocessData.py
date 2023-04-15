from imports import *
def getBondsData():
    df = pd.read_csv('bonds.csv')
    return df


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



def getPortfolioAllocation(df):
    portfolio_allocation = df.groupby('issuer_name').sum()['price']
    return portfolio_allocation

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

def generateCashFlow(coupon_rate, duration, price):
    cash_flows = []
    coupon = coupon_rate * price
    for i in range(int(duration)):
        cash_flows.append(coupon)
    cash_flows.append(price + coupon)
    return cash_flows

def generateYield(coupon_rate, duration, price):
    cash_flows = generateCashFlow(coupon_rate, duration, price)
    ytm = sp.optimize.newton(ytm_func, 0.01, args=(cash_flows, price), maxiter=1000, tol=1e-6)
    return ytm


def generateBondsCols(df):
    # preprocess data
    df['price'] = df['price'].apply(formatPrice)
    df['price'] = df['price'].apply(priceDefault)
    df['coupon_rate'] = df['coupon_rate'].apply(couponRate)
    df['maturity_date'] = df['maturity_date'].apply(formatDateCols)
    df['issue_date'] = df['issue_date'].apply(formatDateCols)
    df['duration'] = (df['maturity_date'] - df['issue_date']).dt.days / 365
    print(df.info())
    print(df)

    # calculate yield
    df['yield'] = df.apply(lambda x: generateYield(x['coupon_rate'], x['duration'], x['price']), axis=1)
    # calculate return
    df['return'] = df['yield'] - df['coupon_rate']

    return df
