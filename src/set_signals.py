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
        months = int(input("Enter how many months ago i should take into account.")) 
        verification_months = input(f"You want to take into account a graph with the last {months} months. Is that right?").lower()
        if verification_months == 'y':
            return months
        else: 
            return 0
    except ValueError:
        print("Invalid input. Enter a number")
        return 0
    

if __name__ == "__main__":
    username = input("What's your name?")
    
    while stockname == "":
        stockname = register_stockname()
    while time_take_account == 0:
        time_take_account = get_time()
    print(stockname)
    print(time_take_account)