import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Thermometer(
        id='my-thermometer',
        value=5,
        min=0,
        max=10,
        style={
            'margin-bottom': '5%'
        }
    ),
    dcc.Slider(
        id='thermometer-slider',
        value=5,
        min=0,
        max=10,

    ),
])


@app.callback(
    dash.dependencies.Output('my-thermometer', 'value'),
    [dash.dependencies.Input('thermometer-slider', 'value')])
def update_thermometer(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)



'''
import dash_design_kit as ddk
import dash_daq as daq
daq.Thermometer(
    min=95,
    max=105,
    value=100,
    showCurrentValue=True,
    units="C"
)



import dash_design_kit as ddk
import dash_daq as daq
daq.Thermometer(
    value=5,
    height=150,
    width=5
)




import dash_design_kit as ddk
import dash_daq as daq
daq.Thermometer(
    value=5,
    label='Current temperature',
    labelPosition='top'
)  



import dash_design_kit as ddk
import dash_daq as daq
daq.Thermometer(
    value=5,
    scale={'start': 2, 'interval': 3,
    'labelInterval': 2, 'custom': {
        '2': 'ideal temperature',
        '5': 'projected temperature'
    }}
)  





'''