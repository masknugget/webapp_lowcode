'''
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns]
)

dash_table.DataTable(
    style_cell={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    data=df_election.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df_election.columns]
)

app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns]
)

app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'lineHeight': '15px'
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns]
)

app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 15px;
            max-height: 30px; min-height: 30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
    ],
    tooltip_duration=None,

    style_cell={'textAlign': 'left'} # left align text in columns for readability
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0
    }
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_cell_conditional=[
        {'if': {'column_id': 'Date'},
         'width': '30%'},
        {'if': {'column_id': 'Region'},
         'width': '30%'},
    ]
)

html.Div([
    html.Div('10%', style={'backgroundColor': 'hotpink', 'color': 'white', 'width': '10%'}),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns if c != 'Date'],
        style_cell_conditional=[
            {'if': {'column_id': 'Region'},
             'width': '10%'}
        ]
    )
])



'''