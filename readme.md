# Stock Signal

This is Stock Signal, a simple program that gets a trendline from you and notifies you via Telegram every time the stock hits this trendline.

## User Manual

1. Run _main.py_
2. Enter your name.
3. Enter official abreviation of the symbol.
4. Enter how many months you want to see in the graph. The points you will input next should be in this period of time. Just the number.
5. Enter _x_ and _y_ axis of two points in the line. X coordinate should be in the following format: (yyyy-mm-dd). Y coordinate should be an integer. The program is designed this way so you can get two points from an already ploted trendline in a platform made to plot.
6. A chart will then be showed to you. To continue saving this trendline you should close the chart.
7. Enter a label for the trendline and it will be saved to data/trendlines.json
