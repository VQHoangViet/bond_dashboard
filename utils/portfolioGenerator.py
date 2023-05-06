from imports import *
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
