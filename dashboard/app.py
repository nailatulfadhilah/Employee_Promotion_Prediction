import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import requests 


from elements.header import header_values 
from elements.row_1 import row1_values
from elements.row_2 import row2_values
from elements.row_3 import row3_values
from elements.prediction import prediction_values

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.title = "Employee Promotion Prediction"


app.layout = dbc.Container([
    header_values(), 
    row1_values(), 
    row2_values(), 
    row3_values(),
    prediction_values()
], fluid=True)