import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from mapping import (
    edu_keys, 
    gender_keys, 
    dept_keys,
    wilayah_keys
)

def row1_values():
    return dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Gender'),
                        html.H1(id="gender-dropdown-value", children="Female"), 
                        dcc.Dropdown(
                            id='gender-dropdown',
                            options=[{'label': i, 'value': i} for i in gender_keys],
                            value='Female', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Age'),
                        html.H1(id="age-slider-value", children="25"), 
                        dcc.Slider(
                            id='age-slider',
                            min=20,
                            max=60,
                            value=25, 
                            marks={str(age): str(age) for age in range(20,60,10)},
                            step=1,
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Education'),
                        html.H1(id="edu-dropdown-value", children="Bachelor's"), 
                        dcc.Dropdown(
                            id='edu-dropdown',
                            options=[{'label': i, 'value': i} for i in edu_keys],
                            value="Bachelor's", 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Region/Wilayah'),
                        html.H1(id="reg-dropdown-value", children="wilayah_1"), 
                        dcc.Dropdown(
                            id='reg-dropdown',
                            options=[{'label': i, 'value': i} for i in wilayah_keys],
                            value="wilayah_1", 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3)
    ], className='mb-2')