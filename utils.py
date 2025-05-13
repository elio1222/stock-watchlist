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

def choice(userchoice):
    match userchoice:
        case 1:
            home()
        case 2:
             investing()
        case 3:
            print("Quitting program...")
def home():
    print("Total Value of Portfolio: ")
    print("Sectors: ")

def investing():
    print("Investing.")