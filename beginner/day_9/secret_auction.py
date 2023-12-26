

print("Welcome to the secret auction")

add_bidders = True
bidders = {}
winning_bidder = {}

while add_bidders:
  name = input("What is your name? ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  more_participants = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if more_participants == 'yes':
    add_bidders = True
  else:
    add_bidders = False

bids = [bidders[name] for name in bidders]
max_bid = max(bids)

for bidder in bidders:
  if max_bid == bidders[bidder]:
    winning_bidder[bidder] = max_bid
    print(f"Winner: {bidder}. Bid: {max_bid}")

  
  
  
