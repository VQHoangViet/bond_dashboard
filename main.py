from imports import *
import preprocessData as ppd

# Load bond data into a pandas dataframe
df = ppd.getBondsData()

# Generate additional bond data columns
df = ppd.generateBondsCols(df)

# Calculate portfolio allocation by issuer
portfolio_allocation = ppd.getPortfolioAllocation(df)



# Create yield curve line chart
fig1 = px.line(df, x='maturity_date', y='yield', color='issuer_name', title='Yield Curve by Issuer')

# Create bond performance scatter plot
fig2 = px.scatter(df, x='return', y='duration', color='issuer_name', title='Bond Performance by Issuer')

# Create credit rating distribution histogram
fig3 = px.histogram(df, x='credit_rating', title='Credit Rating Distribution')

# Create portfolio allocation pie chart
fig4 = px.pie(portfolio_allocation, values='market_value', names=portfolio_allocation.index, title='Portfolio Allocation by Sector')

# Create news feed using Reuters
news_feed = html.Iframe(src='https://www.reuters.com/news/archive/bondsNews', height='600', width='100%')

# Build dashboard using Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Bond Dashboard'),
    html.Div([
        dcc.Graph(id='graph1', figure=fig1),
        dcc.Graph(id='graph2', figure=fig2),
        dcc.Graph(id='graph3', figure=fig3),
        dcc.Graph(id='graph4', figure=fig4),
        html.Div(news_feed),
    ], className='row'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
