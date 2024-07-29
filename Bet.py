user_amount = 1000
user_bet_amount = 0

#Initializes the users bet
def bet_amount():
    global user_amount
    global user_bet_amount
    print("You currently have: " + str(user_amount))
    user_bet_amount = int(input("Enter how much you would like to bet: "))
    user_amount -= user_bet_amount

#Gives the user their payout
def payout():
    global user_amount
    global user_bet_amount
    user_amount += user_bet_amount * 2
    print("You now have: " + str(user_amount))

#Gives the user their payout if they hit a blackjack
def blackjack_payout():
    global user_amount
    global user_bet_amount
    user_amount += user_bet_amount * 2.5
    print("You now have: " + str(user_amount))



