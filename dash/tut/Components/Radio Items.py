import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)



import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)

