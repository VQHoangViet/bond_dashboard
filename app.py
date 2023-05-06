from imports import *

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


nav_contents = []
for page in dash.page_registry.values():
    nav_contents.append(dbc.NavItem(dbc.NavLink(page['name'], href=page["relative_path"], active=True)))


header = dbc.Navbar(
    dbc.Container(
        [
              
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("VN Governance Bonds", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(nav_contents[0]),
                                dbc.NavItem(nav_contents[1]),
                                dbc.NavItem(
                                    nav_contents[2],
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto"
                                ),
                                dbc.NavItem(dbc.NavLink("Help")),
                                dbc.NavItem(dbc.NavLink("About")),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1", 
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
    
)



app.layout = html.Div(
    [header, dbc.Container(dash.page_container, className="mt-0",
                            fluid=True),]
)


if __name__ == '__main__':
	app.run_server(debug=True)