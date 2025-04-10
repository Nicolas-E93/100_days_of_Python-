from logo import silent_auction_logo

print(silent_auction_logo)

name = input("What's your name?\n")
bid = int(input("what is your bid\n"))

bidder_data = {
    "name": name,
    "bid": bid}

print(bidder_data)