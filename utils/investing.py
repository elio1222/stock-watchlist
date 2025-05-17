import yfinance as yf
from collections import Counter
from classes import stock
import matplotlib.pyplot as plt

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