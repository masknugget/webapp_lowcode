import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.LEDDisplay(
        id='my-LED-display',
        label="Default",
        value=6
    ),
    dcc.Slider(
        id='my-LED-display-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])


@app.callback(
    dash.dependencies.Output('my-LED-display', 'value'),
    [dash.dependencies.Input('my-LED-display-slider', 'value')]
)
def update_output(value):
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)



'''
import dash_design_kit as ddk
import dash_daq as daq

daq.LEDDisplay(
    label="Label",
    labelPosition='bottom',
    value='12:34'
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.LEDDisplay(
    label="Large",
    value="9:34",
    size=64,
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.LEDDisplay(
    label="color",
    value='1.001',
    color="#FF5E5E"
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.LEDDisplay(
    label="color",
    value='1.001',
    backgroundColor="#FF5E5E"
)





'''