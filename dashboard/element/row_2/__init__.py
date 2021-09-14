import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from mapping import (
    edu_keys, 
    gender_keys, 
    dept_keys,
    wilayah_keys
)

def row2_values():
    return dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Departemen'),
                        html.H1(id="departemen-dropdown-value", children="Analytics"), 
                        dcc.Dropdown(
                            id='departemen-dropdown',
                            options=[{'label': i, 'value': i} for i in dept_keys],
                            value='Analytics', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Recruitment'),
                        html.H1(id="recruitment-dropdown-value", children="Sourcing"), 
                        dcc.Dropdown(
                            id='recruitment-dropdown',
                            options=[{'label': i, 'value': i} for i in ['Sourcing','Other','Referred']],
                            value='Sourcing', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Period of Employment'),
                        html.H1(id="masa-kerja-slider-value", children="2"), 
                        dcc.Slider(
                            id='masa-kerja-slider',
                            min=0,
                            max=40,
                            value='2', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Number of Trainings'),
                        html.H1(id="jumlah-training-slider-value", children="5"), 
                        dcc.Slider(
                            id='jumlah-training-slider',
                            min=1,
                            max=10,
                            value='5', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3)
    ], className='mb-2')