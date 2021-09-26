import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from mapping import dept_keys


def row2_values():
    return dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Departement'),
                        html.H1(id="departemen-dropdown-value",
                                children="Technology"),
                        dcc.Dropdown(
                            id='departemen-dropdown',
                            options=[{'label': i, 'value': i}
                                     for i in dept_keys],
                            value='Technology',
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Recruitment'),
                        html.H1(id="recruitment-dropdown-value",
                                children="Sourcing"),
                        dcc.Dropdown(
                            id='recruitment-dropdown',
                            options=[{'label': i, 'value': i} for i in
                                     ['Sourcing', 'Other', 'Referred']],
                            value='Sourcing',
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Period of Employment'),
                        html.H1(id="masakerja-slider-value", children="2"),
                        dcc.Slider(
                            id='masakerja-slider',
                            min=0,
                            max=40,
                            value=2,
                            marks={str(period): str(period) for period in range(0, 40, 10)},
                            step=1,
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Number of Trainings'),
                        html.H1(id="jumlahtraining-slider-value", children="5"),
                        dcc.Slider(
                            id='jumlahtraining-slider',
                            min=1,
                            max=10,
                            value=5,
                            marks={str(training): str(training) for training in range(1, 10, 2)},
                            step=1,
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign': 'center'})
                ]),
                ], width=3)
    ], className='mb-2')
