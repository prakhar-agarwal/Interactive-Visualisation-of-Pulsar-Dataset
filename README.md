# nanograv-gsoc

A simple exercise using these data would be to plot, for example, Period vs. Period Derivative, which is a very common plot made by pulsar astronomers (typically, period is on the horizontal axis, and period derivative is on the vertical axis, and period derivative is plotted in logarithm).

1. Pulsar:  this is the pulsar's name 
2. TOAs: the number of "times-of-arrival" we have for the pulsar (these are pulsar timing data points)
3. Raw Profiles: the number of raw data files we have for the pulsar
4. Period: The pulsar's rotation period, in units of seconds [s]
5. Period Derivative: The pulsar's spin-down rate, in units of seconds/seconds [s/s]
6. DM: The pulsar's dispersion measure, in units of parsecs/cubic centimetre [pc/cc]
7. RMS: The root-mean-square value of the pulsar's timing residuals, in usints of microseconds [us]
8. Binary: States whether pulsar is in a binary system.  Y for yes, "-" for no.

Dataset Source: http://msi.mcgill.ca/GSoC_NANOGrav/pulsar_data_test.json


Features:

1. > Used ijson(Iterative JSON parser with a standard Python iterator interface): Instead of loading the whole file into memory and parsing everything at once, it uses iterators to lazily load the data. In that way, when we pass by a key that we don’t need, we can just ignore it and the generated object can be removed from memory.
This way it is possible to use the above script for Streaming data inputs and large static files, without any changes.

2. > Plots a graph for Period vs Period Derivative on a log scale
3. > Mouse hovering revealS data for each data point
4. > Plot permits zooming in and out with dynamic axis labelling
5. > Pressing shift key allows user to view the selected data points on the adjacent graph pane
6. > Box Zoom and Wheel zoom into a selected block
7. > Resizing the plot area for better viewability


Future Task:

1. Integrating Python-Flask to enable Dynamic relevant Data Source URL specification by the user
2. Sliders to select a part of data to be displayed based upon lower and upper bound selected by user

