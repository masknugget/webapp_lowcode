'''

- app.py
- assets/
    |-- typography.css
    |-- header.css
    |-- custom-script.js


app.py

    import dash
    import dash_core_components as dcc
    import dash_html_components as html

    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.Div(
            className="app-header",
            children=[
                html.Div('Plotly Dash', className="app-header--title")
            ]
        ),
        html.Div(
            children=html.Div([
                html.H5('Overview'),
                html.Div('''
                    This is an example of a simple Dash app with
                    local, customized CSS.
                ''')
            ])
        )
    ])
    
    if __name__ == '__main__':
        app.run_server(debug=True)

typography.css

    body {
        font-family: sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: hotpink
    }

header.css

    .app-header {
        height: 60px;
        line-height: 60px;
        border-bottom: thin lightgrey solid;
    }
    
    .app-header .app-header--title {
        font-size: 22px;
        padding-left: 5px;
    }

custom-script.js

    alert('If you see this alert, then your custom JavaScript script has run!')

'''


import dash
import dash_html_components as html

app = dash.Dash(
    __name__,
    assets_external_path='http://your-external-assets-folder-url/'
)
app.scripts.config.serve_locally = False


'''
- app.py
- assets/
    |-- image.png
    

import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Img(src='/assets/image.png')
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
import base64
import dash
import dash_html_components as html

app = dash.Dash(__name__)

image_filename = 'my-image.png'

def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

app.layout = html.Img(src=b64_image(image_filename))




import dash
import dash_html_components as html


# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

app.layout = html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)

'''


'''
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(id='blank-output'),
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
])


app.clientside_callback(
    """
    function(tab_value) {
        if (tab_value === 'tab-1') {
            document.title = 'Tab 1'
        } else if (tab_value === 'tab-2') {
            document.title = 'Tab 2'
        }
    }
    """,
    Output('blank-output', 'children'),
    Input('tabs-example', 'value')
)

if __name__ == '__main__':
    app.run_server(debug=True)

'''


