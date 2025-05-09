import yfinance as yf
import matplotlib.pyplot as plt
username = "username"
stockname = ""
time_take_account = 0

def register_stockname():
    user_input = input(f"Well, hello {username}, which stock are you interested in? Just write the official abreviation. ").upper()
    verification_stock_name = input(f"You entered: {user_input}. Is that right?(y/n) ").lower()
    
    if verification_stock_name != "y":
         return ""
    else: 
         return user_input
         

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
    

def get_stock_data(s_name, s_time):
    data = yf.download(s_name, period=s_time, interval="1d")
    print(data)
    return data.index, data["Low"]


def plot_chart():
    plt.plot(x, y, marker = '')
    plt.xlabel("Day")
    plt.ylabel("Price (pesos)")
    plt.title("Lows chart")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    username = input("What's your name? ")
    
    while stockname == "":
        stockname = register_stockname()
    while time_take_account == 0:
        time_take_account = get_time()
    
    months = f"{time_take_account}mo"

    x, y = get_stock_data(stockname, months)
    plot_chart()

