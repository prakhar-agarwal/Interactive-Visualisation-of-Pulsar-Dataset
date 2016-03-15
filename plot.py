#!/usr/bin/env python

import numpy as np
import pandas as pd
import datetime
import urllib
import ijson
from bokeh.plotting import *
from bokeh.models import CustomJS,HoverTool,ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from collections import OrderedDict


DEFAULT_TICKERS = ['TOAs','RawProfiles', 'Period', 'PeriodDerivative', 'DM', 'RMS', 'Binary']

Pulsar,TOAs,RawProfiles, Period, PeriodDerivative, DM, RMS, Binary=[],[],[],[],[],[],[],[]
url_location=urllib.urlopen('http://msi.mcgill.ca/GSoC_NANOGrav/pulsar_data_test.json')
for item in ijson.items(url_location,"item"):
	Pulsar.append(str(item["Pulsar"]))
	TOAs.append(float(item["TOAs"]))
	RawProfiles.append(int(item["Raw Profiles"]))
	Period.append(float(item["Period"]))
	PeriodDerivative.append(float(item["Period Derivative"]))
	DM.append(str(item["DM"]))
	RMS.append(str(item["RMS"]))
	if (item["Binary"]=="Y"):
		Binary.append("Y")
	else:
		Binary.append("-")


TOOLS = "tap,resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select,previewsave,hover"

s1 = ColumnDataSource(
    data=dict(
        Pulsar=Pulsar,
        TOAs=TOAs,
        RawProfiles=RawProfiles,
        Period=Period,
	PeriodDerivative=PeriodDerivative,
	DM=DM,
	RMS=RMS,
	Binary=Binary,
    )
)

p1 = figure(plot_width=600, plot_height=600,
           title="Period vs Period Derivative", y_axis_type="log" ,y_range=[min(PeriodDerivative)-min(PeriodDerivative)/10, max(PeriodDerivative)+max(PeriodDerivative)/10],x_range=[min(Period)-min(Period)/10, max(Period)+max(Period)/10],x_axis_label='Period', y_axis_label='Period Derivative',tools=TOOLS)
p1.background_fill_color = "beige"
p1.background_fill_alpha = "0.5"
p1.circle('Period', 'PeriodDerivative', legend="period deri",alpha=1.2, source=s1)
p1.xaxis.axis_label_text_font_size = "15pt"
p1.yaxis.axis_label_text_font_size = "15pt"

# Custom data source for selected points
s2 = ColumnDataSource(
    data=dict(
        Pulsar=[],
        TOAs=[],
        RawProfiles=[],
        Period=[],
	PeriodDerivative=[],
	DM=[],
	RMS=[],
	Binary=[],
    )
)




p2= figure(plot_width=600, plot_height=600,
           title=" Selected points from Period vs Period Derivative", y_axis_type="log" ,y_range=[min(PeriodDerivative)-min(PeriodDerivative)/10, max(PeriodDerivative)+max(PeriodDerivative)/10],x_range=[min(Period)-min(Period)/10, max(Period)+max(Period)/10],x_axis_label='Period', y_axis_label='Period Derivative',tools=TOOLS)
p2.xaxis.axis_label_text_font_size = "15pt"
p2.yaxis.axis_label_text_font_size = "15pt"

p2.circle('Period', 'PeriodDerivative', legend="period deri",alpha=1.2, source=s2)

s1.callback = CustomJS(args=dict(s2=s2), code="""
        var inds = cb_obj.get('selected')['1d'].indices;
        var d1 = cb_obj.get('data');
        var d2 = s2.get('data');
        d2['Pulsar'] = []
        d2['TOAs'] = []
        d2['RawProfiles'] = []
        d2['Period'] = []
        d2['PeriodDerivative'] = []
        d2['DM'] = []
        d2['RMS'] = []
        d2['Binary'] = []
        for (i = 0; i < inds.length; i++) {
            d2['Pulsar'].push(d1['Pulsar'][inds[i]])
            d2['TOAs'].push(d1['TOAs'][inds[i]])
            d2['RawProfiles'].push(d1['RawProfiles'][inds[i]])
            d2['Period'].push(d1['Period'][inds[i]])
            d2['PeriodDerivative'].push(d1['PeriodDerivative'][inds[i]])
            d2['DM'].push(d1['DM'][inds[i]])
            d2['RMS'].push(d1['RMS'][inds[i]])
            d2['Binary'].push(d1['Binary'][inds[i]])

        }
        s2.trigger('change');
  """  )



hover = p1.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
	('Pulsar', '@Pulsar'),
	('TOAs', '@TOAs'),
	('RawProfiles', '@RawProfiles'),
	('Period', '@Period'),
	('PeriodDerivative', '@PeriodDerivative'),
    ('DM', '@DM'),
    ('RMS', '@RMS'),
    ('Binary', '@Binary'),
])

# output to static HTML file
output_file("GSoC_NANOGrav.html")


# Set up plots
layout = hplot(p1, p2)

# show the results
show(layout)