import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div(
    [
        html.Button("Download Excel", id="btn_xlsx"),
        dcc.Download(id="download-dataframe-xlsx"),
    ]
)

import pandas as pd
import xlsxwriter

df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 1, 5, 6], "c": ["x", "x", "y", "y"]})


@app.callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "mydf.xlsx", sheet_name="Sheet_name_1")


if __name__ == "__main__":
    app.run_server(debug=True)

    