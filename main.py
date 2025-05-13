from src.set_signals import *
import sys
def run():
    username = "username"
    stockname = ""
    time_take_account = 0
    username = input("What's your name? ")
    label = ""
    while stockname == "":
        stockname = register_stockname(username)
    while time_take_account == 0:
        time_take_account = get_time()
    
    months = f"{time_take_account}mo"

    x, y = get_stock_data(stockname, months)
    plot_chart(x, y)
    
    x1, y1, x2, y2 = get_points()
    m, b = get_slope(x1, y1, x2, y2)
    plot_line(x, m, b)
    plt.show()
    save_yn = input("Save?(y/n) ").lower()
    
    if save_yn == 'y':
        while label == "":
            label = input("Enter a label for this trendline.")
        save_trendline(stockname, label, m, b)
    else:
        sure_yn = input("Are you sure? The program will close!(y/n) ")
        if sure_yn == 'y':
            sys.exit("Exiting")
        else:
            while label == "":
                label = input("Enter a label for this trendline.")
            save_trendline(stockname, label, m, b)

if __name__ == "__main__":
    run()