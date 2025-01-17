print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
''')
other = 'yes'
bids = {}
while other == 'yes':
    name = input("What is the bidder's name?\n")
    bid = int(input("What is the bid price? $"))
    bids[name] = bid
    print("your bid has been stored")
    other = input("Would anyone else like to place a bid?\n")
print(f"The winner is {list(bids.keys())[list(bids.values()).index(max(bids.values()))]} with a ${max(bids.values())} bid!")
