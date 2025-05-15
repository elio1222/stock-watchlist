from classes import stock
import  yfinance as yf
from io import StringIO
import utils
i = 0

'''
amzn = yf.Ticker("AMZN")

for k, v in amzn.info.items():
    print(f"Key: {k} Value: {v}")

'''
'''
amznytd = amzn.history(period = "ytd")['Open'].iloc[0]
print(f"AMZN current price: ${amzn.info['currentPrice']}")
print(f"AMZN YTD price: ${amznytd}")
ytd = amzn.info['currentPrice'] - amznytd
percent = round(((amzn.info['currentPrice'] / amznytd ) * 100) - 100, 2)
print(f"YTD: {ytd} {percent}%")
'''
file_path = 'portfolio.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

file_content = file_content.replace('\n', ' ')
size = len(file_content)
# print(file_content)
buffer = []
share = []
j = 0
stocks = []

while size > j:
    if file_content[j].isalpha():
        buffer.append(file_content[j])
        j = j + 1
        while file_content[j].isalpha() or file_content[j] == "_":
            buffer.append(file_content[j])
            j = j + 1
            token = ''.join(buffer)
        if token == "symbol" and file_content[j] == ":" and file_content[j + 1] == " ":
            j = j + 2
            buffer.clear()
            token = ""
            if file_content[j].isalpha():
                buffer.append(file_content[j])
                j = j + 1
                while file_content[j].isalpha():
                    buffer.append(file_content[j])
                    j = j + 1
                if file_content[j] == " ":
                    token = ''.join(buffer)
                    share.append(token)
                    buffer.clear()
                    token = ""
                    j = j + 1
        if token == "shares" and file_content[j] == ":" and file_content[j + 1] == " ":
            j = j + 2
            buffer.clear()
            token = ""
            if file_content[j].isnumeric() or file_content[j] == ".":
                buffer.append(file_content[j])
                j = j + 1
                while file_content[j].isnumeric() or file_content[j] == ".":
                    buffer.append(file_content[j])
                    j = j + 1
                if file_content[j] == " ":
                    token = ''.join(buffer)
                    share.append(token)
                    buffer.clear()
                    token = ""
                    j = j + 1
                    numofshares = float(share[1])
        if token == "avg_price" and file_content[j] == ":" and file_content[j + 1] == " ":
            j = j + 2
            buffer.clear()
            token = ""
            if file_content[j].isnumeric() or file_content[j] == ".":
                buffer.append(file_content[j])
                j = j + 1
                while file_content[j].isnumeric() or file_content[j] == ".":
                    buffer.append(file_content[j])
                    j = j + 1
                if file_content[j] == " ":
                    token = ''.join(buffer)
                    share.append(token)
                    buffer.clear()
                    token = ""
                    j + 1
                    price = float(share[2])
                    stocks.append(stock(share[0], float(share[1]), float(share[2])))
                    share.clear()
    elif file_content[j] == " ":
        j = j + 1
    elif file_content[j] == "-":
        break

# Displays the users portfolio

'''
for x in stocks:
    print(f"Ticker: {x.get_symbol()} Shares: {x.get_shares()} Avg Cost: ${x.get_price()}")
'''

'''
i = yf.Ticker(stocks[0].get_symbol())
print(i.info)
for k, v in i.info.items():
    print(f"{k}: {v}")
'''
# Provides a menu to see portfolio
userchoice = utils.printmenu()
utils.choice(userchoice, stocks)