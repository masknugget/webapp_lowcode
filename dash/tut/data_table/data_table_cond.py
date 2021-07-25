'''
df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[
        {'name': 'Date', 'id': 'Date', 'type': 'datetime', 'editable': False},
        {'name': 'Delivery', 'id': 'Delivery', 'type': 'datetime'},
        {'name': 'Region', 'id': 'Region', 'type': 'text'},
        {'name': 'Temperature', 'id': 'Temperature', 'type': 'numeric'},
        {'name': 'Humidity', 'id': 'Humidity', 'type': 'numeric'},
        {'name': 'Pressure', 'id': 'Pressure', 'type': 'any'},
    ],
    editable=True,
    style_data_conditional=[
        {
            'if': {
                'column_id': 'Region',
            },
            'backgroundColor': 'dodgerblue',
            'color': 'white'
        },
        {
            'if': {
                'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                'column_id': 'Humidity'
            },
            'backgroundColor': 'tomato',
            'color': 'white'
        },

        {
            'if': {
                'column_id': 'Pressure',

                # since using .format, escape { with {{
                'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max())
            },
            'backgroundColor': '#85144b',
            'color': 'white'
        },

        {
            'if': {
                'row_index': 5,  # number | 'odd' | 'even'
                'column_id': 'Region'
            },
            'backgroundColor': 'hotpink',
            'color': 'white'
        },

        {
            'if': {
                'filter_query': '{id} = 4',  # matching rows of a hidden column with the id, `id`
                'column_id': 'Region'
            },
            'backgroundColor': 'RebeccaPurple'
        },

        {
            'if': {
                'filter_query': '{Delivery} > {Date}', # comparing columns to each other
                'column_id': 'Delivery'
            },
            'backgroundColor': '#3D9970'
        },

        {
            'if': {
                'column_editable': False  # True | False
            },
            'backgroundColor': 'rgb(240, 240, 240)',
            'cursor': 'not-allowed'
        },

        {
            'if': {
                'column_type': 'text'  # 'text' | 'any' | 'datetime' | 'numeric'
            },
            'textAlign': 'left'
        },

        {
            'if': {
                'state': 'active'  # 'active' | 'selected'
            },
           'backgroundColor': 'rgba(0, 116, 217, 0.3)',
           'border': '1px solid rgb(0, 116, 217)'
        }

    ]
)






'''



'''
from dash_table.Format import Format, Sign


app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                'column_id': 'Humidity'
            },
            'color': 'tomato',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{Pressure} > 19',
                'column_id': 'Pressure'
            },
            'textDecoration': 'underline'
        }
    ]
)

# -*- coding: utf-8 -*-

df['Rating'] = df['Humidity'].apply(lambda x:
    '⭐⭐⭐' if x > 30 else (
    '⭐⭐' if x > 20 else (
    '⭐' if x > 10 else ''
)))
df['Growth'] = df['Temperature'].apply(lambda x: '↗️' if x > 0 else '↘️')
df['Status'] = df['Temperature'].apply(lambda x: '🔥' if x > 0 else '🚒')
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
)



'''



'''
# Highlighting the max value in a column
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max()),
                'column_id': 'Pressure'
            },
            'backgroundColor': '#FF4136',
            'color': 'white'
        },
    ]
)


app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{Temperature}} = {}'.format(df['Temperature'].min()),
            },
            'backgroundColor': '#FF4136',
            'color': 'white'
        },
    ]
)


app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    style_data_conditional=(
        [
            {
                'if': {
                    'filter_query': '{{Temperature}} = {}'.format(i),
                    'column_id': 'Temperature',
                },
                'backgroundColor': '#0074D9',
                'color': 'white'
            }
            for i in df['Temperature'].nlargest(3)
        ] +
        [
            {
                'if': {
                    'filter_query': '{{Pressure}} = {}'.format(i),
                    'column_id': 'Pressure',
                },
                'backgroundColor': '#7FDBFF',
                'color': 'white'
            }
            for i in df['Pressure'].nsmallest(3)
        ]
    )
)


def highlight_max_row(df):
    df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    return [
        {
            'if': {
                'filter_query': '{{id}} = {}'.format(i),
                'column_id': col
            },
            'backgroundColor': '#3D9970',
            'color': 'white'
        }
        # idxmax(axis=1) finds the max indices of each row
        for (i, col) in enumerate(
            df_numeric_columns.idxmax(axis=1)
        )
    ]

df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=highlight_max_row(df)
)



'''


'''
def style_row_by_top_values(df, nlargest=2):
    numeric_columns = df.select_dtypes('number').drop(['id'], axis=1).columns
    styles = []
    for i in range(len(df)):
        row = df.loc[i, numeric_columns].sort_values(ascending=False)
        for j in range(nlargest):
            styles.append({
                'if': {
                    'filter_query': '{{id}} = {}'.format(i),
                    'column_id': row.keys()[j]
                },
                'backgroundColor': '#39CCCC',
                'color': 'white'
            })
    return styles

df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=style_row_by_top_values(df)
)


def style_table_by_max_value(df):
    if 'id' in df:
        numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    else:
        numeric_columns = df.select_dtypes('number')
    max_across_numeric_columns = numeric_columns.max()
    max_across_table = max_across_numeric_columns.max()
    styles = []
    for col in max_across_numeric_columns.keys():
        if max_across_numeric_columns[col] == max_across_table:
            styles.append({
                'if': {
                    'filter_query': '{{{col}}} = {value}'.format(
                        col=col, value=max_across_table
                    ),
                    'column_id': col
                },
                'backgroundColor': '#39CCCC',
                'color': 'white'
            })
    return styles


df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=style_table_by_max_value(df)
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{2018} >= 5 && {2018} < 10',
                'column_id': '2018'
            },
            'backgroundColor': '#B10DC9',
            'color': 'white'
        }
    ]
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{{col}}} >= 5 && {{{col}}} < 10'.format(col=col),
                'column_id': col
            },
            'backgroundColor': '#B10DC9',
            'color': 'white'
        } for col in df.columns
    ]
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{{}}} >= {}'.format(col, value),
                'column_id': col
            },
            'backgroundColor': '#B10DC9',
            'color': 'white'
        } for (col, value) in df.quantile(0.9).iteritems()
    ]
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{{}}} <= {}'.format(col, value),
                'column_id': col
            },
            'backgroundColor': '#B10DC9',
            'color': 'white'
        } for (col, value) in df.quantile(0.1).iteritems()
    ]
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=(
        [
            {
                'if': {
                    'filter_query': '{{{}}} > {}'.format(col, value),
                    'column_id': col
                },
                'backgroundColor': '#3D9970',
                'color': 'white'
            } for (col, value) in df.quantile(0.1).iteritems()
        ] +
        [
            {
                'if': {
                    'filter_query': '{{{}}} <= {}'.format(col, value),
                    'column_id': col
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            } for (col, value) in df.quantile(0.5).iteritems()
        ]
    )
)

def highlight_above_and_below_max(df):
    df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    mean = df_numeric_columns.mean().mean()
    return (
        [
            {
                'if': {
                    'filter_query': '{{{}}} > {}'.format(col, mean),
                    'column_id': col
                },
                'backgroundColor': '#3D9970',
                'color': 'white'
            } for col in df_numeric_columns.columns
        ] +
        [
            {
                'if': {
                    'filter_query': '{{{}}} <= {}'.format(col, mean),
                    'column_id': col
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            } for col in df_numeric_columns.columns
        ]
    )

df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if 'id' not in df],
    style_data_conditional=highlight_above_and_below_max(df)
)


df = df_with_none
app.layout = html.Div([
    html.Pre(repr(df)),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_data_conditional=(
            [
                {
                    'if': {
                        'filter_query': '{{{}}} is blank'.format(col),
                        'column_id': col
                    },
                    'backgroundColor': 'tomato',
                    'color': 'white'
                } for col in df.columns
            ]
        )
    )
])

from dash_table.Format import Format

df = df_with_none
app.layout = html.Div([
    html.Pre(repr(df)),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[
            {
                'name': i,
                'id': i,
                'type': 'numeric',
                'format': Format(
                    nully='N/A'
                )
            } for i in df.columns
        ],
        editable=True
    )
])
from dash_table.Format import Format
df = df_with_none
df = df.fillna('N/A').replace('', 'N/A')
app.layout = html.Div([
    html.Pre(repr(df)),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        editable=True,
        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{{{col}}} = "N/A"'.format(col=col),
                    'column_id': col
                },
                'backgroundColor': 'tomato',
                'color': 'white'
            } for col in df.columns
        ]
    )
])
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {'name': i, 'id': i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Region} contains "New"'
            },
            'backgroundColor': '#0074D9',
            'color': 'white'
        }
    ]
)
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {'name': i, 'id': i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Region} = "San Francisco"'
            },
            'backgroundColor': '#0074D9',
            'color': 'white'
        }
    ]
)


'''


'''
import dash_html_components as html

def discrete_background_color_bins(df, n_bins=5, columns='all'):
    import colorlover
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == 'all':
        if 'id' in df:
            df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
        else:
            df_numeric_columns = df.select_dtypes('number')
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [
        ((df_max - df_min) * i) + df_min
        for i in bounds
    ]
    styles = []
    legend = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        backgroundColor = colorlover.scales[str(n_bins)]['seq']['Blues'][i - 1]
        color = 'white' if i > len(bounds) / 2. else 'inherit'

        for column in df_numeric_columns:
            styles.append({
                'if': {
                    'filter_query': (
                        '{{{column}}} >= {min_bound}' +
                        (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                    ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                    'column_id': column
                },
                'backgroundColor': backgroundColor,
                'color': color
            })
        legend.append(
            html.Div(style={'display': 'inline-block', 'width': '60px'}, children=[
                html.Div(
                    style={
                        'backgroundColor': backgroundColor,
                        'borderLeft': '1px rgb(50, 50, 50) solid',
                        'height': '10px'
                    }
                ),
                html.Small(round(min_bound, 2), style={'paddingLeft': '2px'})
            ])
        )

    return (styles, html.Div(legend, style={'padding': '5px 0 5px 0'}))
    
    
(styles, legend) = discrete_background_color_bins(df_wide, columns=['2018'])

app.layout = html.Div([
    legend,
    dash_table.DataTable(
        data=df.to_dict('records'),
        sort_action='native',
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_data_conditional=styles
    )
])

def data_bars(df, column):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    ranges = [
        ((df[column].max() - df[column].min()) * i) + df[column].min()
        for i in bounds
    ]
    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100
        styles.append({
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'background': (
                """
                    linear-gradient(90deg,
                    #0074D9 0%,
                    #0074D9 {max_bound_percentage}%,
                    white {max_bound_percentage}%,
                    white 100%)
                """.format(max_bound_percentage=max_bound_percentage)
            ),
            'paddingBottom': 2,
            'paddingTop': 2
        })

    return styles


def data_bars_diverging(df, column, color_above='#3D9970', color_below='#FF4136'):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    col_max = df[column].max()
    col_min = df[column].min()
    ranges = [
        ((col_max - col_min) * i) + col_min
        for i in bounds
    ]
    midpoint = (col_max + col_min) / 2.

    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        min_bound_percentage = bounds[i - 1] * 100
        max_bound_percentage = bounds[i] * 100

        style = {
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'paddingBottom': 2,
            'paddingTop': 2
        }
        if max_bound > midpoint:
            background = (
                """
                    linear-gradient(90deg,
                    white 0%,
                    white 50%,
                    {color_above} 50%,
                    {color_above} {max_bound_percentage}%,
                    white {max_bound_percentage}%,
                    white 100%)
                """.format(
                    max_bound_percentage=max_bound_percentage,
                    color_above=color_above
                )
            )
        else:
            background = (
                """
                    linear-gradient(90deg,
                    white 0%,
                    white {min_bound_percentage}%,
                    {color_below} {min_bound_percentage}%,
                    {color_below} 50%,
                    white 50%,
                    white 100%)
                """.format(
                    min_bound_percentage=min_bound_percentage,
                    color_below=color_below
                )
            )
        style['background'] = background
        styles.append(style)

    return styles

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=(
        data_bars(df, 'lifeExp') +
        data_bars(df, 'gdpPercap')
    ),
    style_cell={
        'width': '100px',
        'minWidth': '100px',
        'maxWidth': '100px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    page_size=20
)

df_gapminder['gdpPercap relative values'] = df_gapminder['gdpPercap']
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=(
        data_bars(df, 'gdpPercap relative values') + [{
            'if': {'column_id': 'gdpPercap relative values'},
            'color': 'transparent'
        }]
    ),
    style_cell={
        'width': '100px',
        'minWidth': '100px',
        'maxWidth': '100px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    page_size=20
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=(
        data_bars_diverging(df, 'lifeExp') +
        data_bars_diverging(df, 'gdpPercap')
    ),
    style_cell={
        'width': '100px',
        'minWidth': '100px',
        'maxWidth': '100px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    page_size=20
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {'name': i, 'id': i}
        if i != 'Date' else
        {'name': 'Date', 'id': 'Date', 'type': 'datetime'}
        for i in df.columns
    ],
    style_data_conditional=[{
        'if': {'filter_query': '{Date} datestartswith "2015-10"'},
        'backgroundColor': '#85144b',
        'color': 'white'
    }]
)


'''

