import dash
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Knob(
        id='my-knob',
    ),
    html.Div(id='knob-output')
])


@app.callback(
    dash.dependencies.Output('knob-output', 'children'),
    [dash.dependencies.Input('my-knob', 'value')])
def update_output(value):
    return 'The knob value is {}.'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)


'''
import dash_design_kit as ddk
import dash_daq as daq

daq.Knob(
    size=140,
    value=3
)  


import dash_design_kit as ddk
import dash_daq as daq

daq.Knob(
    max=100,
    value=3
)  


import dash_design_kit as ddk
import dash_daq as daq

daq.Knob(
  label="Color Ranges",
  value=3,
  color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}}
)


import dash_design_kit as ddk
import dash_daq as daq

daq.Knob(
  label="Gradient Ranges",
  value=7,
  color={"gradient":True,"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}}
) 


import dash_design_kit as ddk
import dash_daq as daq

daq.Knob(
  label="Scale",
  value=7,
  max=18,
  scale={'start':0, 'labelInterval': 3, 'interval': 3}
) 



'''