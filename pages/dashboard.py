
from imports import *

dash.register_page(__name__)

# Load the data into a pandas DataFrame
df = pd.read_csv('./data/VietnamGovernanceBonds.csv')




# table 
grid = dag.AgGrid(
    id="bond-table-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth":125},
    columnSize="sizeToFit",
)

# Create the app and set the layout
layout = html.Div(

    dbc.Container(
        [
            dbc.Row(
                [
                    # dropdown
                    dcc.Dropdown(id='currency-dropdown', options=[
                        {'label': c, 'value': c} for c in df['currency_type'].unique()
                    ], value='VND'),
                ], className='mt-2'
            ),

            dbc.Row(
                [
                    # charts
                    dcc.Graph(id="volume-chart"),
                ], className='mt-2'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id="payment-chart"),
                        ], className='col-4'
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="rate-histogram"),
                        ], className='col-8'
                    ),
                ]
            ),

            dbc.Row(   
                [
                    # table 
                    html.Div([grid], style={'height': '300px', 'width': '100%'}),
                ], className='mt-2'

            ),





            
            # html.Div([
            #     # dropdown
            #     dcc.Dropdown(id='currency-dropdown', options=[
            #         {'label': c, 'value': c} for c in df['currency_type'].unique()
            #     ], value='VND'),
            #     # charts
            #     dcc.Graph(id="volume-chart"),
            #     dcc.Graph(id="payment-chart"),
            #     dcc.Graph(id="rate-histogram"),

            # ]),


            # table 
            # html.Div([grid], style={'height': '300px', 'width': '100%'}, className='row'),

        ],
        fluid=True, class_name='mt-0'
    ),

)



# Define the callbacks


@callback(
    Output("bond-table-grid", "children"), Input("bond-table-body", "cellClicked")
)
def display_cell_clicked_on(cell):
    if cell is None:
        return "Click on a cell"
    return f"clicked on cell value:  {cell['value']}, column:   {cell['colId']}, row index:   {cell['rowIndex']}"


@callback(
    Output("volume-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_volume_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.line(filtered_df, x="bond_code", y="outstanding_volume", title="Outstanding Volume")
    return fig

@callback(
    Output("payment-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_payment_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    counts = filtered_df.groupby(["interest_payment_method", "interest_payment_type"]).size().reset_index(name="count")
    fig = px.pie(counts, values="count", names="interest_payment_type", hole=.3, title="Interest Payment Type")
    return fig

@callback(
    Output("rate-histogram", "figure"),
    [Input("currency-dropdown", "value")])
def update_rate_histogram(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.histogram(filtered_df, x="coupon_rate", nbins=20, title="Coupon Rate Distribution")
    return fig


@callback(
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
