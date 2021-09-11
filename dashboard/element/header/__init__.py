import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import date 
import dash_html_components as html

def header_values(): 
    return dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H1("Emplotee Promotion Prediction"), 
                html.H2("AUC = 0.96")
            ], style={"textAlign": "center"})
        ], width=10)],
        className="mb-2 mt-2")