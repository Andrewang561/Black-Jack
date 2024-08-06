import BlackJack
import json

user_amount = 1000
user_bet_amount = 0

#Initializes the users bet
def bet_amount():
    global user_amount
    global user_bet_amount
    print("You currently have: " + str(user_amount))
    user_bet_amount = int(input("Enter how much you would like to bet: "))
    if user_bet_amount <= user_amount:
        user_amount -= user_bet_amount
    else:
        print("Insufficient Funds!")
        bet_amount()

#Gives the user their payout
def payout():
    global user_amount
    global user_bet_amount
    user_amount += user_bet_amount * 2
    print("You now have: " + str(user_amount))

# Returns the players bet when a tie occurs
def tie():
    global user_amount
    global user_bet_amount
    user_amount += user_bet_amount
    print("You now have: " + str(user_amount))

#Gives the user their payout if they hit a blackjack
def blackjack_payout():
    global user_amount
    global user_bet_amount
    user_amount += user_bet_amount * 2.5
    print("You hit BlackJack!")
    print("You now have: " + str(user_amount))
    BlackJack.play_again()

# Saves users current betting amount to a file
def save_bets(user_amount):
    json_bet_amount = json.dumps(user_amount, indent=4)
    with open("users bet amount", "w") as outfile:
        outfile.write(json_bet_amount)



