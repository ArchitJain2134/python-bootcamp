import art
print(art.logo)

bid = {}
continue_bidding = True

def comparision(bid_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("Highest bidder is ", winner, "with a bid of ", highest_bid)


while continue_bidding:
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n"))
    bid[name] = price
    should_continue = input("Are there any other bidder? Type 'yes' or 'no' \n").lower()

    # if condition to break the while loop when all the entries are taken
    if should_continue == "no":
        continue_bidding = False
        comparision(bid)
    elif should_continue == "yes":
        print("\n"* 100)
