import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
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


@app.callback(
    Output("promotion-prediction-values", "children"),
    Output("gender-dropdown-value", "children"),
    Output("age-slider-value", "children"),
    Output("edu-dropdown-value", "children"),
    Output("reg-dropdown-value", "children"),
    Output("departemen-dropdown-value", "children"),
    Output("recruitment-dropdown-value", "children"),
    Output("masakerja-slider-value", "children"),
    Output("jumlahtraining-slider-value", "children"),
    Output("rating-slider-value", "children"),
    Output("penghargaan-dropdown-value", "children"),
    Output("kpi-dropdown-value", "children"),
    Output("trainingscore-slider-value", "children"),
    Input("gender-dropdown", "value"),
    Input("age-slider", "value"),
    Input("edu-dropdown", "value"),
    Input("reg-dropdown", "value"),
    Input("departemen-dropdown", "value"),
    Input("recruitment-dropdown", "value"),
    Input("masakerja-slider", "value"),
    Input("jumlahtraining-slider", "value"),
    Input("rating-slider", "value"),
    Input("penghargaan-dropdown", "value"),
    Input("kpi-dropdown", "value"),
    Input("trainingscore-slider", "value")
)
def get_prediction_output(gender_value, age_value, edu_value,
                          reg_value, departemen_value,
                          recruitment_value, masakerja_value,
                          jumlahtraining_value, rating_value,
                          penghargaan_value, kpi_value,
                          trainingscore_value):
    input_json = {
        "wilayah": reg_value,
        "pendidikan": edu_value,
        "jenis_kelamin": gender_value,
        "jumlah_training": jumlahtraining_value,
        "umur": age_value,
        "rating_tahun_lalu": rating_value,
        "masa_kerja": masakerja_value,
        "KPI": kpi_value,
        "penghargaan": penghargaan_value,
        "rata_rata_skor_training": trainingscore_value,
        "departemen": departemen_value,
        "rekrutmen": recruitment_value
    }

    req = requests.post(url="http://127.0.0.1:8000/predict", json=input_json)
    result = req.json().get("prediction")
    return result, str(gender_value), str(age_value), str(edu_value), str(reg_value), str(departemen_value), str(recruitment_value), str(masakerja_value), str(jumlahtraining_value), str(rating_value), str(penghargaan_value), str(kpi_value), str(trainingscore_value)


if __name__ == "__main__":
    app.server.run(host="127.0.0.1", port=8001, debug=False, threaded=False)
