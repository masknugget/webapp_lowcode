'''

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
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
    value=[3, 7.65]
)

import dash_design_kit as ddk
import dash_core_components as dcc

# RangeSlider has included=True by default
dcc.RangeSlider(
    min=0,
    max=100,
    value=[10, 65],
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    }
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=100,
    value=[10, 65],
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    },
    included=False
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[1, 3, 4, 5, 12, 17]
)

import dash_design_kit as ddk
import dash_core_components as dcc
dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15, 17, 20],
    pushable=2
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[10, 15],
    allowCross=False
)

'''

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import *
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Use the following function when accessing the value of 'my-range-slider'
# in callbacks to transform the output value to logarithmic
def transform_value(value):
    return 10 ** value


app.layout = html.Div([
    dcc.RangeSlider(
        id='non-linear-range-slider',
        marks={i: '{}'.format(10 ** i) for i in range(4)},
        max=3,
        value=[0.1, 2],
        dots=False,
        step=0.01,
        updatemode='drag'
    ),
    html.Div(id='output-container-range-slider-non-linear', style={'margin-top': 20})
])


@app.callback(
    Output('output-container-range-slider-non-linear', 'children'),
    Input('non-linear-range-slider', 'value'))
def update_output(value):
    transformed_value = [transform_value(v) for v in value]
    return 'Linear Value: {}, Log Value: [{:0.2f}, {:0.2f}]'.format(
        str(value),
        transformed_value[0],
        transformed_value[1]
    )


if __name__ == '__main__':
    app.run_server(debug=True)

    