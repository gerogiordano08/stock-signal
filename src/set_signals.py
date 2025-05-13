import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
import pandas as pd

username = "username"
stockname = ""
time_take_account = 0

# register_stockname() asks the user for the stockname and returns it. Its used to define 'stockname'.
def register_stockname(username):
    user_input = input(f"Well, hello {username}, which stock are you interested in? Just write the official abreviation. ").upper()
    verification_stock_name = input(f"You entered: {user_input}. Is that right?(y/n) ").lower()
    
    if verification_stock_name != "y":
         return ""
    else: 
         return user_input
         
# get_time() asks the user for the months to plot the chart and returns it. Its used to define 'time_take_account' and later 'months'.
def get_time():
    try:
        months = int(input("Enter how many months ago i should take into account. ")) 
        verification_months = input(f"You want to take into account a graph with the last {months} months. Is that right? ").lower()
        if verification_months == 'y':
            return months
        else: 
            return 0
    except ValueError:
        print("Invalid input. Enter a number")
        return 0
    
# get_stock_data uses 'stockname' and 'months' to get data from yahoo finance and returns the data index(dates) and a data column(prices). Its used to define 'x' and 'y', which will be used to plot a chart.
def get_stock_data(s_name, s_time):
    data = yf.download(s_name, period=s_time, interval="1d")
    print(data)
    return data.index, data["Low"]

# plot_chart() uses 'x' and 'y' to plot a chart and a function with data(prices) from a stock.
def plot_chart(x, y):
    plt.plot(x, y, marker = '')
    plt.xlabel("Day")
    plt.ylabel("Price (pesos)")
    plt.title("Lows chart")
    plt.grid(True)
    plt.suptitle("Close and go back to console to choose whether to save. ", fontsize=10, color="gray")

#get_points() asks the user for the coordinates of two points of a trend line(already drawn in Trendview) and returns the coordinates as values.
def get_points():
    print("I need two points of the trend line to define it.")
    p1x = input("Enter x axis(yyyy-mm-dd) of point 1: ")
    p1y = input("Enter y axis(price) of point 1: ")
    p2x = input("Enter x axis(yyyy-mm-dd) of point 2: ")
    p2y = input("Enter y axis(price) of point 2: ")
    return p1x, p1y, p2x, p2y

# get_slope() uses the coordinates from get_points() and returns the slope and y_intersection of the trend line.
def get_slope(x1, y1, x2, y2):
    d1 = datetime.strptime(x1, "%Y-%m-%d").toordinal()
    d2 = datetime.strptime(x2, "%Y-%m-%d").toordinal()
    y1, y2 = int(y1), int(y2)
    slope = (y2-y1)/(d2-d1)
    y_inter = -slope*d1+y1
    return slope, y_inter

# plot_line() uses the slope and y_intersection from get_slope() and defines the affine function, and plots it.
def plot_line(x, m, b):

    affine_y = [m * xi.toordinal() + b for xi in x]
    plt.plot(x, affine_y, label="Trend Line", linestyle= "--")

def save_trendline(symbol, m, b, file_path="data/trendlines.json"):
    if os.path.exists:
        with open(file_path, "r") as f:
            trendlines = json.load(f)
    else:
        trendlines = {}
    trendlines[symbol] = {
        "m" : m, 
        "b" : b
    }
    with open(file_path, "w") as f:
        json.dump(trendlines, f, indent=4)
    print(f"Trendline for {symbol} saved.")

def compare_trendline_w_data(symbol, json_path="data/trendlines.json"):
    with open(json_path, "r") as f:
        trendlines = json.load(f)

    m = trendlines[symbol]["m"]
    b = trendlines[symbol]["b"]
    today = datetime.today().toordinal()
    trendline_price = m*today + b
    symbol_data = yf.download(symbol, period="2d", interval="1d", progress=False)

    actual_price = symbol_data["Low"].iloc[1].item()
    yest_price = symbol_data["Low"].iloc[0].item()
    close_price = symbol_data["Close"].iloc[1].item()

    higher_than_yest = False
    if yest_price < actual_price:
        higher_than_yest = True

    dif_1 = actual_price - trendline_price
    dif_2 = trendline_price - actual_price
    cercania = pd.to_numeric(close_price * 0.009)

    if 0 < dif_1 <= cercania and higher_than_yest == False:
        return "tocando-arriba"
    elif 0 < dif_1 <= cercania and higher_than_yest:
        return "cruzo-p-arriba"
    elif 0 < dif_2 <= cercania and higher_than_yest:
        return "tocando-abajo"
    elif 0 < dif_2 <= cercania and higher_than_yest == False:
        return "cruzo-p-abajo"
