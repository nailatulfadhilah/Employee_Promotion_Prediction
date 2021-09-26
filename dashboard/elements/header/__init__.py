import dash_bootstrap_components as dbc
import dash_html_components as html


def header_values():
    return dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H1("Employee Promotion Prediction"),
                html.H2("AUC = 0.96")
            ], style={"textAlign": "center"})
                ], width=12)],
        className="mb-2 mt-2")
