from bokeh.plotting import output_file, figure, show
import json
from collections import Counter

with open("birthdays.json", "r") as jfile:
	birthdays = json.load(jfile)

date = []
for k, v in birthdays.items():
	date.append(v[3:5])

data = dict(Counter(date))

x = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
y = [0 for i in range(12)]
for i in data:
	y[int(i)-1] = data[i]

myTools ="pan,wheel_zoom,reset,resize,lasso_select,hover,click,undo"

output_file("primo.html")

plott = figure(tools = myTools, title = "Birthdays frequencies", x_range = x, x_axis_label = "Months", y_axis_label = "Count")

plott.vbar(x=x, top=y, width=0.5)

show(plott)