# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import time

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(id="output-1"),
        dcc.Input(id="input-1", value="Input triggers local spinner"),
        html.Div(
            [
                html.Div(id="output-2"),
                dcc.Input(id="input-2", value="Input triggers nested spinner"),
            ]
        ),
    ]
)


@app.callback(Output("output-1", "children"), Input("input-1", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value


@app.callback(Output("output-2", "children"), Input("input-2", "value"))
def input_triggers_nested(value):
    time.sleep(1)
    return value


if __name__ == "__main__":
    app.run_server(debug=False)