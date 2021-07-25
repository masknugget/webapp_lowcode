import dash
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Slider(
        id='my-daq-slider-ex',
        value=17
    ),
    html.Div(id='slider-output')
])


@app.callback(
    dash.dependencies.Output('slider-output', 'children'),
    [dash.dependencies.Input('my-daq-slider-ex', 'value')])
def update_output(value):
    return 'The slider is currently at {}.'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)



'''
import dash_design_kit as ddk
import dash_daq as daq
daq.Slider(
    min=0, max=100, value=30,
    marks={'25': 'mark', '50': '50'}
)



import dash_design_kit as ddk
import dash_daq as daq
daq.Slider(
    size=50
)  



import dash_design_kit as ddk
import dash_daq as daq

daq.Slider(
    id='my-daq-slider',
    value=17,
    handleLabel='Handle'
) 



import dash_design_kit as ddk
import dash_daq as daq
daq.Slider(
    min=0,
    max=100,
    value=50,
    handleLabel={"showCurrentValue": True,"label": "VALUE"},
    step=10
) 



import dash_design_kit as ddk
import dash_daq as daq
daq.Slider(
    vertical=True
)  






'''