from imports import *

dash.register_page(__name__, path='/')

# Create news feed using Reuters
news_feed = html.Iframe(src='https://www.reuters.com/news/archive/bondsNews', height='100%',
                         width='100%', 
                            style={'border': 'none',
                                   'margin': '0px',
                                   'padding': '0px'}
                         )

# Create the app and set the layout
layout = html.Div(
    dbc.Container(
    [
        #news feed
        html.Div([
            # Wrap the news_feed iframe and your dashboard in a container with full screen height
            html.Div(news_feed, style={'height': '100vh',}),
        ]),
    ],
    fluid=True, class_name='mt-0'
    ),
)


 