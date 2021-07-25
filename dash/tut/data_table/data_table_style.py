# dash_table.DataTable(
#     data=df.to_dict('records'),
#     columns=[{'id': c, 'name': c} for c in df.columns],
# )
#


'''
dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_cell={'textAlign': 'left'},
    style_cell_conditional=[
        {
            'if': {'column_id': 'Region'},
            'textAlign': 'left'
        }
    ]
)


dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],

    style_as_list_view=True,
)




dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_as_list_view=True,
    style_cell={'padding': '5px'},
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
)



dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
)


dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year"},
        {"name": ["City", "Montreal"], "id": "montreal"},
        {"name": ["City", "Toronto"], "id": "toronto"},
        {"name": ["City", "Ottawa"], "id": "ottawa"},
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
    merge_duplicate_headers=True,
)


dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
)



dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],

    style_as_list_view=True,
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
)


dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_header={ 'border': '1px solid black' },
    style_cell={ 'border': '1px solid grey' },
)

dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_data={ 'border': '1px solid blue' },
    style_header={ 'border': '1px solid pink' },
)

dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {'id': c, 'name': c, 'editable': (c == 'Humidity')}
        for c in df.columns
    ],
    style_data_conditional=[{
        'if': {'column_editable': False},
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white'
    }],
    style_header_conditional=[{
        'if': {'column_editable': False},
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white'
    }],
)





'''