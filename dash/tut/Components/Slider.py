import dash_design_kit as ddk
import dash_core_components as dcc

dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3
)


import dash_design_kit as ddk
import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)

import dash_design_kit as ddk
import dash_core_components as dcc

dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)

