import dash_html_components as html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])

import dash_core_components as dcc

dcc.Markdown('''
#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
''')




import dash_html_components as html

html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})



'''
    html.A
    html.Abbr
    html.Acronym
    html.Address
    html.Area
    html.Article
    html.Aside
    html.Audio
    html.B
    html.Base
    html.Basefont
    html.Bdi
    html.Bdo
    html.Big
    html.Blink
    html.Blockquote
    html.Br
    html.Button
    html.Canvas
    html.Caption
    html.Center
    html.Cite
    html.Code
    html.Col
    html.Colgroup
    html.Command
    html.Content
    html.Data
    html.Datalist
    html.Dd
    html.Del
    html.Details
    html.Dfn
    html.Dialog
    html.Div
    html.Dl
    html.Dt
    html.Element
    html.Em
    html.Embed
    html.Fieldset
    html.Figcaption
    html.Figure
    html.Font
    html.Footer
    html.Form
    html.Frame
    html.Frameset
    html.H1
    html.H2
    html.H3
    html.H4
    html.H5
    html.H6
    html.Header
    html.Hgroup
    html.Hr
    html.I
    html.Iframe
    html.Img
    html.Ins
    html.Isindex
    html.Kbd
    html.Keygen
    html.Label
    html.Legend
    html.Li
    html.Link
    html.Listing
    html.Main
    html.MapEl
    html.Mark
    html.Marquee
    html.Meta
    html.Meter
    html.Multicol
    html.Nav
    html.Nextid
    html.Nobr
    html.Noscript
    html.ObjectEl
    html.Ol
    html.Optgroup
    html.Option
    html.Output
    html.P
    html.Param
    html.Picture
    html.Plaintext
    html.Pre
    html.Progress
    html.Q
    html.Rb
    html.Rp
    html.Rt
    html.Rtc
    html.Ruby
    html.S
    html.Samp
    html.Script
    html.Section
    html.Select
    html.Shadow
    html.Slot
    html.Small
    html.Source
    html.Spacer
    html.Span
    html.Strike
    html.Strong
    html.Sub
    html.Summary
    html.Sup
    html.Table
    html.Tbody
    html.Td
    html.Template
    html.Textarea
    html.Tfoot
    html.Th
    html.Thead
    html.Time
    html.Title
    html.Tr
    html.Track
    html.U
    html.Ul
    html.Var
    html.Video
    html.Wbr
    html.Xmp
    
'''