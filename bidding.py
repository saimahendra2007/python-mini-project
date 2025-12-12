logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def to_find_winner(bidding_dictionary):
    highest_value = 0
    for bidder in bidding_dictionary:
        bidding_value = bidding_dictionary[bidder]
        bidding_value>highest_value
        highest_value=bidding_value
        winner = bidder
        print(bidding_dictionary)
    print(f"the winner is {winner} of the bidding value of ${highest_value}")
bids = {}
continue_bidding = True
while continue_bidding:
    name= input("what is your name?")
    bid = int(input("what is your bid amount?"))
    bids[name]=bid
    wheather_continue = input("are the anyother bidder in the room?\n if there type 'yes' or 'no'").lower()
    if wheather_continue =='no':
        to_find_winner(bids)
        print("thanking for participating in the aution.\n The aution ends here!!")
        exit()
    elif wheather_continue =='yes':
        print('\n'*20)













    