# import dash_design_kit as ddk
# import dash_core_components as dcc
# from datetime import date
#
# dcc.DatePickerSingle(
#     id='date-picker-single',
#     date=date(1997, 5, 10)
# )

'''
# Display Format Examples
import dash_design_kit as ddk
import dash_core_components as dcc

dcc.DatePickerSingle(
    date='2017-06-21',
    display_format='MMM Do, YY'
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017,6,21),
    display_format='M-D-Y-Q',
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017,6,21),
    display_format='MMMM Y, DD'
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017,6,21),
    display_format='X',
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='MMM Do, YY',
    placeholder='MMM Do, YY',
    date=date(2017,6,21)
)


import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='M-D-Y-Q',
    placeholder='M-D-Y-Q',
    date=date(2017,6,21)
)

import dash_design_kit as ddk
import dash_core_components as dcc
import datetime

dcc.DatePickerSingle(
    month_format='MMMM Y',
    placeholder='MMMM Y',
    date=datetime.date(2020,2,29)
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='X',
    placeholder='X',
    date=date(2017,6,21)
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    calendar_orientation='vertical',
    placeholder='Select a date',
    date=date(2017,6,21)
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    clearable=True,
    with_portal=True,
    date=date(2017,6,21)
)

import dash_design_kit as ddk
import dash_core_components as dcc
from datetime import date

dcc.DatePickerSingle(
    is_RTL=True,
    first_day_of_week=3,
    date=date(2017,6,21)
)


'''


from datetime import date
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import re

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        date=date(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-single')
])


@app.callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime('%B %d, %Y')
        return string_prefix + date_string

if __name__ == '__main__':
    app.run_server(debug=True)

