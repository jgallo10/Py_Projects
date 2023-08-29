#Creating a slight auction program where the highest bidder wins

bidders = {}
more = "yes"
highest_bidder = ""
highest_bid = 0

while more == "yes":
    name = input("What is your nanme?: \n")
    bid = int(input("What is your bid?: \n"))
    more = input("Are there other bidders?: Type 'yes' or 'no' \n")

    bidders[name] = bid
    print("\x1b[2J]")
    
for person in bidders:
    if bidders[person] > highest_bid:
        highest_bid = bidders[person]
        highest_bidder = person
        
print(f"The winnder is {highest_bidder} with a bid of {highest_bid} \n")
        


