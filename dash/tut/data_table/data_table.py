import dash
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)


'''
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_size=10
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_size=20,  # we have less data in this example, so setting to 20
    style_table={'height': '300px', 'overflowY': 'auto'}
)
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    fixed_rows={'headers': True},
    style_table={'height': 400}  # defaults to 500
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    fixed_rows={'headers': True}
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    fixed_rows={'headers': True},
    style_header={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    fixed_rows={'headers': True},
    style_cell={
        'minWidth': 95, 'maxWidth': 95, 'width': 95
    }
)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    virtualization=True,
    fixed_rows={'headers': True},
    style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
    style_table={'height': 300}  # default is 500
)

'''