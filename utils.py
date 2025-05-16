import yfinance as yf
from collections import Counter

from requests import HTTPError

from classes import stock
import matplotlib.pyplot as plt


def printmenu():
    choice = 0

    while choice < 1 or choice > 4:
        print("""
Stock Watchlist Program.
1. Home
2. Investing
3. Create a Watchlist
4. Quit""")
        choice = int(input("Enter a menu option: "))

    return choice

def choice(stocks):
    quit = False
    while not quit:
        userchoice = printmenu()
        match userchoice:
            case 1:
                home(stocks)
            case 2:
                 investing(stocks)
            case 3:
                watchlist()
            case 4:
                quit = True
                print("Quitting program...")
def home(stocks):
    returntomenu = False
    while not returntomenu:
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
            '''
            info = ticker.info
            if not symbol == "VOO":
                price = info.get('currentPrice')
            else:
                price = ticker.fast_info.last_price
                '''
            price = ticker.fast_info['lastPrice']
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
            # info = ticker.info
            pastprice = ticker.history(period = "5d")['Open'].iloc[0]
            currentprice = ticker.fast_info['lastPrice']
            pasttotal = pasttotal + pastprice * shares
            currenttotal = currenttotal + currentprice * shares
            past5dtotal = currenttotal - pasttotal
        print(f"Total Gain/Loss of Portfolio Past Week: ${round(past5dtotal,2)}")

        for i in stocks:
            symbol = i.get_symbol()
            shares = i.get_shares()
            ticker = yf.Ticker(symbol)
            # info = ticker.info
            pastprice = ticker.history(period = "1mo")['Open'].iloc[0]
            currentprice = ticker.fast_info['lastPrice']
            pasttotal = pasttotal + pastprice * shares
            currenttotal = currenttotal + currentprice * shares
            past1mtotal = currenttotal - pasttotal

        print(f"Total Gain/Loss of Portfolio Past Month: ${round(past1mtotal,2)}")

        for i in stocks:
            symbol = i.get_symbol()
            shares = i.get_shares()
            ticker = yf.Ticker(symbol)
            # info = ticker.info
            pastprice = ticker.history(period="ytd")['Open'].iloc[0]
            currentprice = ticker.fast_info['lastPrice']
            pasttotal = pasttotal + pastprice * shares
            currenttotal = currenttotal + currentprice * shares
            ytd = currenttotal - pasttotal
        print(f"Total Gain/Loss of Portfolio YTD: ${round(ytd,2)}")
        sectors = []
        symbols = []
        value = []
        # Below code will print a pie chart of sectors AND the percentages of each stock contributed to the total port
        figs, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 6))
        figs.subplots_adjust(wspace = 0.4)
        for i in stocks:

            try:
                ticker = yf.Ticker(i.get_symbol())
                sectors.append(ticker.info['sector'])
                symbols.append(i.get_symbol())
                value.append(((ticker.fast_info['lastPrice'] * i.get_shares() ) / 100 ) * 100)

            except Exception as e:
                print("yFinance blocked the request. Sector unavailable")

        c = dict(Counter(sectors))
        keys = []
        values = []
        for k, v in c.items():
            keys.append(k)
            values.append(v)
        # axs[0,0].pie(values, labels = keys, autopct = "%.2f%%", pctdistance = 0.8)
        # axs[0,1].pie(value, labels = symbols, autopct = "%.2f%%", pctdistance = 0.8, textprops = {'size': 'smaller'})

        ax1.pie(values, labels=keys, autopct="%.2f%%", pctdistance=0.8, textprops={'fontsize': '12'})
        ax1.set_title('Sectors')

        colors = [
            "#4B5563",  # Charcoal Gray
            "#7C3AED",  # Deep Violet
            "#A16207",  # Brass
            "#10B981",  # Teal
            "#6D28D9",  # Royal Purple
            "#FACC15",  # Mustard Yellow
            "#0F766E",  # Deep Cyan
            "#78350F"   # Saddle Brown
        ]

        ax2.pie(value, labels=symbols, autopct="%.2f%%", pctdistance=0.8, textprops={'fontsize': '7'}, colors=colors)
        ax2.set_title('Portfolio')

        plt.show()
        returnchoice = input("Enter anything to return to the main menu.\n")
        returntomenu = True
        break

def printinvestingmenu():
    print("\nInvesting Screen")
    print("1. View Individual Stocks")
    print("2. View All Positions")
    print("3. Return")
    investingchoice = int(input("Enter a menu option: "))
    return investingchoice

def investing(stocks):
    userchoice = printinvestingmenu()
    returntomenu = False
    while not returntomenu:

        match userchoice:
            case 1:
                for i in stocks:
                    print(f" | {i.get_symbol()}", end=" | ")
                userticker = input("\nEnter the Ticker to View the Individual Stock: ")

                valid = True
                while valid:
                    totalsize = 0
                    for i in stocks:
                        if userticker == i.get_symbol():
                            valid = False
                            numofshares = i.get_shares()
                            avg_price = i.get_price()
                            break
                        else:
                            totalsize = totalsize + 1
                        if totalsize == len(stocks):
                            userticker = input("Enter the Ticker to View the Individual Stock: ")

                chosenstock = yf.Ticker(userticker)
                totalValue = chosenstock.fast_info['lastPrice'] * numofshares
                purchaseValue = numofshares * avg_price
                profitorloss = totalValue - purchaseValue
                percent = round(((totalValue / purchaseValue ) * 100) - 100, 2)
                print(f"Company Name: {chosenstock.info['longName']}, ({userticker})")
                print(f"Total Value: ${round(totalValue,2)}")
                print(f"Shares Owned: {numofshares}")
                print(f"Average Cost: ${avg_price}")
                if profitorloss > 0:
                    print(f"Total Gain/Loss: +${round(profitorloss,2)} (+{percent}%)")
                else:
                    print(f"Total Gain/Loss: ${round(profitorloss,2)} ({percent}%)")
                print(f"Volume: {chosenstock.info['volume']}")
                print(f"Forward PE: {chosenstock.info['forwardPE']}")
                break
            case 2:
                for i in stocks:
                    ticker = i.get_symbol()
                    s = yf.Ticker(ticker)
                    currentValue = s.info['currentPrice'] * i.get_shares()
                    costbasistotal = i.get_shares() * i.get_price()
                    print(f"{ticker} ~ Last Price: ${s.info['currentPrice']} Current Value: ${round(currentValue,2)}")
                    print(f"Quantity: {i.get_shares()} Average Cost Basis: ${i.get_price()}"
                          f" Cost Basis Total: ${round(costbasistotal,2)}\n")
                break
            case 3:
                print("Returning to Main Menu...")
                returntomenu = True
                break
def watchlist():
    userwatchlist = []
    tomenu = False
    while not tomenu:
        print("\nWatchlist Screen")
        print("1. View Watchlist")
        print("2. Add Stock")
        print("3. Delete Stock")
        print("4. Return to Main Menu")

        chosen = int(input("Select an option: "))
        while chosen < 0 or chosen > 4:
            chosen = int(input("Select an option: "))

        match chosen:
            case 1:
                print("Watchlist Overview.")
                if len(userwatchlist) > 0:
                    for i in userwatchlist:
                        ticker = yf.Ticker(i.get_symbol())
                        print("--------------------------------------------------------------")
                        print(f"Ticker: {i.get_symbol()} Last Price: ${round(ticker.fast_info['lastPrice'],2)}")
                        print(f"Open: ${round(ticker.fast_info['open'],2)}")
                        print(f"Previous Close: ${round(ticker.fast_info['previous_close'],2)}")
                        print(f"Day Low: ${round(ticker.fast_info['day_low'],2)}")
                        print(f"Day High: ${round(ticker.fast_info['day_high'],2)}")
                        print(f"Year Low: ${round(ticker.fast_info['year_low'],2)}")
                        print(f"Year High: ${round(ticker.fast_info['year_high'],2)}")
                        print("--------------------------------------------------------------")
                else:
                    print("THERES NOTHING IN YOUR WATCHLIST!!!")
            case 2:
                addticker = input("Enter the ticker of the stock you would like to add: ")
                userwatchlist.append(stock(addticker))
                print(f"{addticker} added.")
            case 3:
                deleteticker = input("Enter the ticker of the stock you would like to delete: ")
                userwatchlist.remove(deleteticker)
                print(f"{deleteticker} removed.")
            case 4:
                print("Returning to Main Menu")
                tomenu = True
                break



