'''
import dash_design_kit as ddk
import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=10,
    step=None,
    marks={
        0: '0 °F',
        3: '3 °F',
        5: '5 °F',
        7.65: '7.65 °F',
        10: '10 °F'
    },
    value=5
)

import dash_design_kit as ddk
import dash_core_components as dcc

# Slider has included=True by default
dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    }
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    },
    included=False
)



'''

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Use the following function when accessing the value of 'my-slider'
# in callbacks to transform the output value to logarithmic
def transform_value(value):
    return 10 ** value


app.layout = html.Div([
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(10 ** i) for i in range(4)},
        max=3,
        value=2,
        step=0.01,
        updatemode='drag'
    ),
    html.Div(id='updatemode-output-container', style={'margin-top': 20})
])


@app.callback(Output('updatemode-output-container', 'children'),
              Input('slider-updatemode', 'value'))
def display_value(value):
    return 'Linear Value: {} | \
            Log Value: {:0.2f}'.format(value, transform_value(value))


if __name__ == '__main__':
    app.run_server(debug=True)

    