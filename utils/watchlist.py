import yfinance as yf
from collections import Counter
from classes import stock
import matplotlib.pyplot as plt

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
                    print("Note: Watchlist will also be written into a file. ")
                    writewatchlist(userwatchlist)

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

def writewatchlist(userwatchlist):
    with open('watchlist.txt', 'w') as file:
        file.write("WATCHLIST OVERVIEW\n")
        for i in userwatchlist:
            ticker = yf.Ticker(i.get_symbol())
            file.write("--------------------------------------------------------------\n")
            file.write(f"Ticker: {i.get_symbol()} Last Price: ${round(ticker.fast_info['lastPrice'], 2)}\n")
            file.write(f"Open: ${round(ticker.fast_info['open'], 2)}\n")
            file.write(f"Previous Close: ${round(ticker.fast_info['previous_close'], 2)}\n")
            file.write(f"Day Low: ${round(ticker.fast_info['day_low'], 2)}\n")
            file.write(f"Day High: ${round(ticker.fast_info['day_high'], 2)}\n")
            file.write(f"Year Low: ${round(ticker.fast_info['year_low'], 2)}\n")
            file.write(f"Year High: ${round(ticker.fast_info['year_high'], 2)}\n")
            file.write("--------------------------------------------------------------\n")
        file.flush()
