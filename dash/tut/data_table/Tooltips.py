'''

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
    ],

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)

'''

'''

app.layout = dash_table.DataTable(
    data=[
        {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
        {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
        {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
    ],
    columns=[
        {'id': 'shop', 'name': 'Store Location'},
        {'id': 'sales', 'name': 'Sales Revenue'},
        {'id': 'goal', 'name': 'Revenue Goal'},
    ],
    tooltip_data=[
        {
            'shop': 'Location at Bakersfield',
            'sales': '$4M in Revenue',
            'goal': {'value': '6M **under** Goal', 'type': 'markdown'}
        },
        {
            'shop': 'Location at Berkeley',
            'sales': '$10M in Revenue',
            'goal': {'value': '9M **over** Goal', 'type': 'markdown'}
        },
        {
            'shop': 'Location at Big Bear Lake',
            'sales': '$5M in Revenue',
            'goal': {'value': '1M **over** Goal', 'type': 'markdown'}
        },
    ],
    tooltip_delay=0,
    tooltip_duration=None
)


df = pd.DataFrame({
    'shop': ['Bakersfield', 'Berkely', 'Big Bear Lake'],
    'sales': [3, 1, 5],
    'goal': [10, 1, 4],
    'address': [
        '3000 Mall View Road, Suite 1107\n\nBakersfield, CA\n\n93306',
        '2130 Center Street, Suite 102\n\nBerkeley, CA\n\n94704',
        '652 Pine Knot Avenue\n\nBig Bear Lake, CA\n\n92315'
    ]
})
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in ['shop', 'sales', 'goal']],
    tooltip_data=[{
        'shop': {'value': row['address'], 'type': 'markdown'},
        'sales': {
            'value': 'Sales were **{} {}** than the goal'.format(
                str(abs(row['goal'] - row['sales'])),
                'less' if row['goal'] > row['sales'] else 'more'
            ),
            'type': 'markdown'
        },
        'goal': 'Goal was {}'.format(
            'not achieved' if row['goal'] > row['sales'] else 'achieved'
        ),
    } for row in df.to_dict('records')],

    tooltip_delay=0,
    tooltip_duration=None
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    tooltip_header={i: i for i in df.columns},

    # Style headers with a dotted underline to indicate a tooltip
    style_header={
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    },

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)


app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    tooltip_header={
        'Rep': 'Republican',
        'Dem': 'Democrat',
        'Ind': 'Independent',
    },

    # Style headers with a dotted underline to indicate a tooltip
    style_header_conditional=[{
        'if': {'column_id': col},
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    } for col in ['Rep', 'Dem', 'Ind']],

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)



app.layout = dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year"},
        {"name": ["City", "Montreal"], "id": "montreal"},
        {"name": ["City", "Toronto"], "id": "toronto"},
        {"name": ["City", "Ottawa"], "id": "ottawa"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[{
        "year": i, "montreal": i * 10, "toronto": i * 100,
        "ottawa": i * -1, "vancouver": i * -10, "temp": i * -100,
        "humidity": i * 5,
    } for i in range(10)],
    merge_duplicate_headers=True,

    tooltip_header={
        'year': ['', 'Year the measurement was taken'],
        'montreal': ['Average Measurements Across City', 'Montreal, QC, Canada'],
        'toronto': ['Average Measurements Across City', 'Toronto, ON, Canada'],
        'ottawa': ['Average Measurements Across City', 'Ottawa, ON, Canada'],
        'vancouver': ['Average Measurements Across City', 'Vancouver, BC, Canada'],
        'temp': ['Average for a Year', 'Celcius'],
        'humidity': ['Average for a Year', 'Percentage'],
    },

    style_header={
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    },
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    tooltip ={i: {
        'value': i,
        'use_with': 'both'  # both refers to header & data cell
    } for i in df.columns},

    # Style headers with a dotted underline to indicate a tooltip
    style_header={
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    },

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': i, 'id': i} for i in df.columns],

    tooltip_conditional=[
        {
            'if': {
                'filter_query': '{Region} contains "New"'
            },
            'type': 'markdown',
            'value': 'This row is significant.'
        }
    ],

    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Region} contains "New"'
            },
            'backgroundColor': '#0074D9',
            'color': 'white',
            'textDecoration': 'underline',
            'textDecorationStyle': 'dotted',
        }
    ],
    tooltip_delay=0,
    tooltip_duration=None
)


'''

'''
app.layout = dash_table.DataTable(
    data=[
        {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
        {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
        {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
    ],
    columns=[
        {'id': 'shop', 'name': 'Store Location'},
        {'id': 'sales', 'name': 'Sales Revenue'},
        {'id': 'goal', 'name': 'Revenue Goal'},
    ],
    tooltip_data=[
        {
            'shop': {
                'value': 'Location at Bakersfield\n\n![Bakersfield]({})'.format(
                    app.get_relative_path('/assets/images/table/bakersfield.jpg')
                ),
                'type': 'markdown'
            }
        },
        {
            'shop': {
                'value': 'Location at Berkeley\n\n![Berkeley]({})'.format(
                    app.get_relative_path('/assets/images/table/berkeley.jpg')
                ),
                'type': 'markdown'
            }
        },
        {
            'shop': {
                'value': 'Location at Big Bear Lake\n\n![Big Bear Lake](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Big_Bear_Valley%2C_California.jpg/1200px-Big_Bear_Valley%2C_California.jpg)',
                'type': 'markdown'
            }
        },
    ],

    # Style headers with a dotted underline to indicate a tooltip
    style_data_conditional=[{
        'if': {'column_id': 'shop'},
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    }],

    tooltip_delay=0,
    tooltip_duration=None
)

'''



'''
markdown_table = """
| City       | Value     | Return     |
| :------------- | :----------: | -----------: |
|  Montreal   | 41,531    | 431.245 |
| Seattle   | 53,153 | 12.431 |
"""

app.layout = dash_table.DataTable(
    data=[
        {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
        {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
        {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
    ],
    columns=[
        {'id': 'shop', 'name': 'Store Location'},
        {'id': 'sales', 'name': 'Sales Revenue'},
        {'id': 'goal', 'name': 'Revenue Goal'},
    ],
    tooltip={
        c: {'value': markdown_table, 'type': 'markdown'}
        for c in ['shop', 'sales', 'goal']
    },
    tooltip_delay=0,
    tooltip_duration=None
)


app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
    ],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: white; font-family: monospace;'
    }],

    tooltip_delay=0,
    tooltip_duration=None
)



'''