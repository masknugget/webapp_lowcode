import dash
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.ToggleSwitch(
        id='my-toggle-switch',
        value=False
    ),
    html.Div(id='toggle-switch-output')
])

@app.callback(
    dash.dependencies.Output('toggle-switch-output', 'children'),
    [dash.dependencies.Input('my-toggle-switch', 'value')])
def update_output(value):
    return 'The switch is {}.'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)


'''
import dash_design_kit as ddk
import dash_daq as daq
daq.ToggleSwitch(
    vertical=True
)  



import dash_design_kit as ddk
import dash_daq as daq
daq.ToggleSwitch(
    size=100
)



import dash_design_kit as ddk
import dash_daq as daq
daq.ToggleSwitch(
    label='My toggle switch',
    labelPosition='bottom'
)





'''