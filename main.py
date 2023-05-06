
from imports import *
# Load the data into a pandas DataFrame
df = pd.read_csv('VietnamGovernanceBonds.csv')

# Preprocess the data


# Create news feed using Reuters
news_feed = html.Iframe(src='https://www.reuters.com/news/archive/bondsNews', height='600', width='100%')
# Create the app and set the layout
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1("Việt Nam Bonds Dashboard"),
    html.Div([
        html.Div(news_feed),
    ], className='row'),
    dcc.Dropdown(id='currency-dropdown', options=[
        {'label': c, 'value': c} for c in df['currency_type'].unique()
    ], value='USD'),
    dcc.Graph(id="volume-chart"),
    dcc.Graph(id="payment-chart"),
    dcc.Graph(id="rate-histogram"),
    html.Table(id="bond-table", children=[
        html.Thead(html.Tr([
            html.Th("Bond Code"),
            html.Th("Issuance Date"),
            html.Th("Maturity Date"),
            html.Th("Remaining Tenor"),
            html.Th("Status")
        ])),
        html.Tbody(id="bond-table-body")
        
    ])
])

# # Create yield curve line chart
# fig1 = px.line(df, x='maturity_date', y='yield', color='issuer_name', title='Yield Curve by Issuer')

# # Create bond performance scatter plot
# fig2 = px.scatter(df, x='return', y='duration', color='issuer_name', title='Bond Performance by Issuer')

# # Create credit rating distribution histogram
# fig3 = px.histogram(df, x='credit_rating', title='Credit Rating Distribution')

# # Create portfolio allocation pie chart
# fig4 = px.pie(portfolio_allocation, values='market_value', names=portfolio_allocation.index, title='Portfolio Allocation by Sector')




# Build dashboard using Dash
# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1('Bond Dashboard'),
#     html.Div([
#         dcc.Graph(id='graph1', figure=fig1),
#         dcc.Graph(id='graph2', figure=fig2),
#         dcc.Graph(id='graph3', figure=fig3),
#         # dcc.Graph(id='graph4', figure=fig4),
#         html.Div(news_feed),
#     ], className='row'),
# ])


# Define the callbacks
@app.callback(
    Output("volume-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_volume_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.line(filtered_df, x="bond_code", y="outstanding_volume")
    return fig

@app.callback(
    Output("payment-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_payment_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    counts = filtered_df.groupby(["interest_payment_method", "interest_payment_type"]).size().reset_index(name="count")
    fig = px.pie(counts, values="count", names="interest_payment_type", hole=.3, title="Interest Payment Type")
    return fig

@app.callback(
    Output("rate-histogram", "figure"),
    [Input("currency-dropdown", "value")])
def update_rate_histogram(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.histogram(filtered_df, x="coupon_rate", nbins=20, title="Coupon Rate Distribution")
    return fig


@app.callback(
    Output("bond-table-body", "children"),
    [Input("currency-dropdown", "value")])
def update_bond_table(currency):
    filtered_df = df[df['currency_type'] == currency]
    rows = []
    for i in range(len(filtered_df)):
        row = html.Tr([
            html.Td(filtered_df.iloc[i]['bond_code']),
            html.Td(filtered_df.iloc[i]['issuance_date']),
            html.Td(filtered_df.iloc[i]['maturity_date']),
            html.Td(filtered_df.iloc[i]['remaining_tenor']),
            html.Td(filtered_df.iloc[i]['status'])
        ])
        rows.append(row)
    return rows

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)