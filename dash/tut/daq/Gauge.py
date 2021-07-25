import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge',
        label="Default",
        value=6
    ),
    dcc.Slider(
        id='my-gauge-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])


@app.callback(
    dash.dependencies.Output('my-gauge', 'value'),
    [dash.dependencies.Input('my-gauge-slider', 'value')]
)
def update_output(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)



'''
import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    value=5,
    label='Default',
    max=20,
    min=0,
)  

import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    showCurrentValue=True,
    units="MPH",
    value=5,
    label='Default',
    max=10,
    min=0,
)  


import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    logarithmic=True,
    value=5,
    label='Default',
    max=10,
    min=0,
)  

import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    color="#9B51E0",
    value=2,
    label='Default',
    max=5,
    min=0,
)  
import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
    value=2,
    label='Default',
    max=10,
    min=0,
) 

import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
    size=200,
    value=2,
    label='Default',

)  

import dash_design_kit as ddk
import dash_daq as daq

daq.Gauge(
  label='Scale',
  scale={'start': 0, 'interval': 3, 'labelInterval': 2},
  value=3,
  min=0,
  max=24,
)  



'''