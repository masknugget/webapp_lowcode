import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.GraduatedBar(
        id='my-graduated-bar',
        label="Default",
        value=6
    ),
    dcc.Slider(
        id='my-graduated-bar-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])


@app.callback(
    dash.dependencies.Output('my-graduated-bar', 'value'),
    [dash.dependencies.Input('my-graduated-bar-slider', 'value')]
)
def update_output(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)


'''
import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    vertical=True,
    value=10
) 


import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    size=200,
    value=10
)  


import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    max=100,
    value=50
)


import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    step=2,
    max=100,
    value=50
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    showCurrentValue=True,
    max=100,
    value=38
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    color={"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
    showCurrentValue=True,
    value=10
)


import dash_design_kit as ddk
import dash_daq as daq

daq.GraduatedBar(
    color={"gradient":True,"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
    showCurrentValue=True,
    value=10
)  





'''