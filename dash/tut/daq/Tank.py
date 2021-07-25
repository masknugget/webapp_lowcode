import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Tank(
        id='my-tank',
        value=5,
        min=0,
        max=10,
        style={'margin-left': '50px'}
    ),
    dcc.Slider(
        id='tank-slider',
        value=5,
        min=0,
        max=10,
    ),
])


@app.callback(
    dash.dependencies.Output('my-tank', 'value'),
    [dash.dependencies.Input('tank-slider', 'value')])
def update_tank(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)



'''
import dash_design_kit as ddk
import dash_daq as daq
daq.Tank(
    value=6,
    showCurrentValue=True,
    units='gallons',
    style={'margin-left': '50px'}
)  


import dash_design_kit as ddk
import dash_daq as daq
daq.Tank(
    height=75,
    width=200,
    value=6,
    style={'margin-left': '50px'}
)



import dash_design_kit as ddk
import dash_daq as daq
daq.Tank(
    value=3,
    label='Tank label',
    labelPosition='bottom'
)  



import dash_design_kit as ddk
import dash_daq as daq
daq.Tank(
    value=3,
    scale={'interval': 2, 'labelInterval': 2,
           'custom': {'5': 'Set point'}},
    style={'margin-left': '50px'}
) 



import dash_design_kit as ddk
import dash_daq as daq
daq.Tank(
    min=0,
    max=10,
    value=300,
    logarithmic=True,
    base=3,
    style={'margin-left': '50px'}
)  




'''