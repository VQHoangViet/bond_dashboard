from imports import *

def getBondsData():
    df = pd.read_csv('VietnamGovernanceBonds.csv')
    return df

def getPortfolioAllocation(df):
    portfolio_allocation = df.groupby('issuer_name').sum()['price'].reset_index()
    return portfolio_allocation