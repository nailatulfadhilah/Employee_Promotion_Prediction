import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from mapping import (
    edu_keys, 
    gender_keys, 
    dept_keys,
    wilayah_keys
)

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
                            value='3', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Win an Awards?'),
                        html.H1(id="penghargaan-dropdown-value", children="NO"), 
                        dcc.Dropdown(
                            id='penghargaan-dropdown',
                            options=[{'label': i, 'value': i} for i in ['YES','NO']],
                            value='NO', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('KPI >80%?'),
                        html.H1(id="kpi-dropdown-value", children="YES"), 
                        dcc.Dropdown(
                            id='KPI-dropdown',
                            options=[{'label': i, 'value': i} for i in ['YES','NO']],
                            value='YES', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Average Trainig Score'),
                        html.H1(id="training-score-slider-value", children="70"), 
                        dcc.Slider(
                            id='training-score-slider',
                            min=0,
                            max=100,
                            value='70', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3)
    ], className='mb-2')