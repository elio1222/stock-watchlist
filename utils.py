import yfinance as yf
from classes import stock


def printmenu():
    choice = 0
    while choice < 1 or choice > 3:
        print("""
Stock Watchlist Program.
1. Home
2. Investing
3. Quit""")
        choice = int(input("Enter a menu option: "))

    return choice

def choice(userchoice, stocks):
    match userchoice:
        case 1:
            home(stocks)
        case 2:
             investing(stocks)
        case 3:
            print("Quitting program...")
def home(stocks):
    print("\nHome Screen")
    total = 0
    pasttotal = 0
    currenttotal = 0
    index = 0
    for i in stocks:
        symbol = i.get_symbol()
        # print(symbol)
        shares = i.get_shares()
        # print(shares)
        ticker = yf.Ticker(symbol)
        info = ticker.info
        if not symbol == "VOO":
            price = info.get('currentPrice')
        else:
            price = ticker.fast_info.last_price
        total = total + price * shares
    print(f"Total Value of Portfolio: ${round(total,2)}")

    for i in stocks:
        # we need to get the individual prices of each stock from a week ago
        # using the history(period + 1week"), then once we have the price from a week ago, we can 
        # multiply that price by the number of shares the user owns then subtract from the current price * 
        # the number of shares the user owns.
        symbol = i.get_symbol()
        shares = i.get_shares()
        ticker = yf.Ticker(symbol)
        info = ticker.info
        pastprice = ticker.history(period = "5d")['Open'].iloc[0]
        currentprice = ticker.info['currentPrice']
        pasttotal = pasttotal + pastprice * shares
        currenttotal = currenttotal + currentprice * shares
        past5dtotal = currenttotal - pasttotal
    print(f"Total Gain/Loss of Portfolio Past Week: ${round(past5dtotal,2)}")

    for i in stocks:
        symbol = i.get_symbol()
        shares = i.get_shares()
        ticker = yf.Ticker(symbol)
        info = ticker.info
        pastprice = ticker.history(period = "1mo")['Open'].iloc[0]
        currentprice = ticker.info['currentPrice']
        pasttotal = pasttotal + pastprice * shares
        currenttotal = currenttotal + currentprice * shares
        past1mtotal = currenttotal - pasttotal

    print(f"Total Gain/Loss of Portfolio Past Month: ${round(past1mtotal,2)}")

    for i in stocks:
        symbol = i.get_symbol()
        shares = i.get_shares()
        ticker = yf.Ticker(symbol)
        info = ticker.info
        pastprice = ticker.history(period="ytd")['Open'].iloc[0]
        currentprice = ticker.info['currentPrice']
        pasttotal = pasttotal + pastprice * shares
        currenttotal = currenttotal + currentprice * shares
        ytd = currenttotal - pasttotal
    print(f"Total Gain/Loss of Portfolio YTD: ${round(ytd,2)}")
    print("Sectors: ")

def printinvestingmenu():
    print("Investing Screen")
    print("1. View Individual Stocks")
    print("2. View All Stocks")
    print("3. Return")
    investingchoice = int(input("Enter a menu option: "))
    return investingchoice
def investing(stocks):
    userchoice = printinvestingmenu()
    match userchoice:
        case 1:
            for i in stocks:
                print(i.get_symbol(), end="~~")
            userticker = input("Enter the Ticker to View the Individual Stock.")
            valid = True
            while valid:
                for i in stocks:
                    if userticker == i.get_symbol():
                        valid = False
                        break
                    elif i == len(stocks):
                        userticker = input("Enter the Ticker to View the Individual Stock.")



