import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


def row3_values():
    return dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Previous Year Rating'),
                        html.H1(id="rating-slider-value", children="3"),
                        dcc.Slider(
                            id='rating-slider',
                            min=0,
                            max=5,
                            value=3,
                            marks={str(rating): str(rating) for rating in range(0, 5, 1)},
                            step=1,
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Win an Awards?'),
                        html.H1(id="penghargaan-dropdown-value", children="NO"),
                        dcc.Dropdown(
                            id='penghargaan-dropdown',
                            options=[{'label': i, 'value': i} for i in ['YES', 'NO']],
                            value='NO',
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('KPI >80%?'),
                        html.H1(id="kpi-dropdown-value", children="YES"),
                        dcc.Dropdown(
                            id='kpi-dropdown',
                            options=[{'label': i, 'value': i} for i in ['YES', 'NO']],
                            value='YES',
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Average Trainig Score'),
                        html.H1(id="trainingscore-slider-value", children="70"),
                        dcc.Slider(
                            id='trainingscore-slider',
                            min=0,
                            max=100,
                            value=70,
                            marks={str(score): str(score) for score in range(0, 100, 20)},
                            step=1,
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3)
    ], className='mb-2')
