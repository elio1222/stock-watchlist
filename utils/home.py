import yfinance as yf
from collections import Counter
from classes import stock
import matplotlib.pyplot as plt

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
