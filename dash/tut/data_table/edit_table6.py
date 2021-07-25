import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='computed-table',
        columns=[
            {'name': 'Input Data', 'id': 'input-data'},
            {'name': 'Input Squared', 'id': 'output-data'}
        ],
        data=[{'input-data': i} for i in range(11)],
        editable=True,
    ),
])


@app.callback(
    Output('computed-table', 'data'),
    Input('computed-table', 'data_timestamp'),
    State('computed-table', 'data'))
def update_columns(timestamp, rows):
    for row in rows:
        try:
            row['output-data'] = float(row['input-data']) ** 2
        except:
            row['output-data'] = 'NA'
    return rows


if __name__ == '__main__':
    app.run_server(debug=True)


'''
dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year", "clearable": "first" },
        {"name": ["City", "Montreal"], "id": "montreal", "deletable": [False, True]},
        {"name": ["City", "Toronto"], "id": "toronto", "renamable": True },
        {"name": ["City", "Ottawa"], "id": "ottawa", "hideable": "last"},
        {"name": ["City", "Vancouver"], "id": "vancouver", "clearable": True, "renamable": True, "hideable": True, "deletable": True },
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "toronto": i * 100,
            "ottawa": i * -1,
            "vancouver": i * -10,
            "temp": i * -100,
            "humidity": i * 5,
        }
        for i in range(10)
    ],
    css=[
        {"selector": ".column-header--delete svg", "rule": 'display: "none"'},
        {"selector": ".column-header--delete::before", "rule": 'content: "X"'}
    ]
)

dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year" },
        {"name": ["City", "Montreal"], "id": "montreal", "deletable": [False, True]},
        {"name": ["City", "Toronto"], "id": "toronto", "renamable": True },
        {"name": ["City", "Ottawa"], "id": "ottawa", "hideable": "last"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "toronto": i * 100,
            "ottawa": i * -1,
            "vancouver": i * -10,
            "temp": i * -100,
            "humidity": i * 5,
        }
        for i in range(10)
    ],
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True
)


'''