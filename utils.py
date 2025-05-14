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
        choice = int(input("Enter the a menu option: "))

    return choice

def choice(userchoice, stocks):
    match userchoice:
        case 1:
            home(stocks)
        case 2:
             investing()
        case 3:
            print("Quitting program...")
def home(stocks):
    print("\nHome Screen")
    total = 0
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
    '''
    print(f"Total Gain/Loss of Portfolio Past Week: $")
    for i in stocks:
        # we need to get the individual prices of each stock from a week ago
        # using the history(period + 1week"), then once we have the price from a week ago, we can 
        # multiply that price by the number of shares the user owns then subtract from the current price * 
        # the number of shares the user owns. 
        indivstock5 = yf.Ticker[i.get_symbol()].history(period = "5d")['Open'].ilec[0]
        indivstocktoday = yf.Ticker[i.get_symbol()].info['currentPrice']
        fivedays = indivstocktoday - indivstock5
    print(fivedays)
    print(f"Total Gain/Loss of Portfolio Past Month: ${}")
    for i in stocks:
        
    print(f"Total Gain/Loss of Portfolio YTD: ${}")
    print("Sectors: ")
    '''

def investing():
    print("Investing.")