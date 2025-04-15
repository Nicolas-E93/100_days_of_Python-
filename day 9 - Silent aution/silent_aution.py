from logo import silent_auction_logo

print(silent_auction_logo)

bidder_data = {}

# Initialize the dictionary before starting the loop
add_player = True
while add_player:

    # Get user input for each new bidder
    name = input("What's your name?\n")
    bid = int(input("what is your bid\n"))

    # Add the bid to the dictionary using the name as the key
    bidder_data[name] = bid

    # Ask the user if they want to add another bidder
    continue_response = input('Are there more players?\n').lower()
    if continue_response == "no":
        add_player = False

print(bidder_data)

# Initialize variables to store the current highest bid and bidder
max_bid = 0
winner = ""

def calculate_max_bidder():
    for bidder in bidder_data:
        if bidder_data[bidder] > max_bid:
            max_bid = bidder_data[bidder]
            winner = bidder

print(f' 🏆The winner of the auction is .... {winner}🏆')




