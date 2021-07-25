import dash
import dash_daq as daq
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Indicator(
        id='my-indicator',
        label="Default",
    ),
    html.Button(
        'On/Off',
        id='my-indicator-button',
        n_clicks=0
    ),
])


@app.callback(
    dash.dependencies.Output('my-indicator', 'value'),
    [dash.dependencies.Input('my-indicator-button', 'n_clicks')]
)
def update_output(value):
    if value % 2 == 0:
        value = True
    else:
        value = False
    return value


if __name__ == '__main__':
    app.run_server(debug=True)


'''
import dash_design_kit as ddk
import dash_daq as daq

daq.Indicator(
  label="Label",
  labelPosition="bottom",
  value=True
)  


import dash_design_kit as ddk
import dash_daq as daq

daq.Indicator(
  label="Off",
  value=False
) 



import dash_design_kit as ddk
import dash_daq as daq

daq.Indicator(
  label="Square",
  width=16,
  height=16
)



import dash_design_kit as ddk
import dash_daq as daq

daq.Indicator(
  label="Purple",
  color="#551A8B",
  value=True
)  




'''