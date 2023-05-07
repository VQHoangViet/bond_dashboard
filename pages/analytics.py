from imports import *
dash.register_page(__name__)

# layout = dbc.Container([

#     dbc.Row(
#         dbc.Col(
#              html.H1(children='This is our Analytics page'),
#                 width=12,
#             ), className='mt-2'
#         ),
    


# 	dbc.Row(
#         dbc.Col(
#             [
#                 "Select a city: ",
#                 dcc.RadioItems(['New York City', 'Montreal','San Francisco'],
#                     id='analytics-input')
#             ], width=12
#         ), className='mt-2'
#     ),
    

# ])

layout = html.Div([
    html.H1(children='This is our Analytics page'),

], style={'background-color': 'red'})


@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'