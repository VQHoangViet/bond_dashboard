from imports import *
def getBondsData():
    df = pd.read_csv('VietnamGovernanceBonds.csv')

    # preprocess data
    # df['price'] = df['price'].apply(ppd.formatPrice)
    # df['price'] = df['price'].apply(ppd.priceDefault)
    
    df['coupon_rate'] = df['coupon_rate'].apply(ppd.couponRate)
    df['maturity_date'] = df['maturity_date'].apply(ppd.formatDateCols)
    df['issue_date'] = df['issue_date'].apply(ppd.formatDateCols)
    df['duration'] = (df['maturity_date'] - df['issue_date']).dt.days / 365

    print(df.info())
    print(df)

    return df

def getPortfolioAllocation(df):
    portfolio_allocation = df.groupby('issuer_name').sum()['price'].reset_index()
    return portfolio_allocation