import random
import Bet
import json

card_list = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3",
    "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7"
    , "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J"
    , "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

dealers_list = []
users_list = []



# Initialize the game for the first time
def initialize(start_button):
    if start_button == "Yes":
        load_file()
        Bet.bet_amount()
        deal_cards()
        if is_blackjack(dealers_list):
            blackjack_loss()
        elif is_blackjack(users_list):
            Bet.blackjack_payout()
        stand_or_hit = input("Stand or Hit: ")
        stand_and_hit(stand_or_hit)
    elif start_button == "No":
        print("Sorry to hear that!")
    else:
        start_button = input("Please Enter Yes or No: ")
        initialize(start_button)

# Loads user saved state if they want
def load_file():
    answer = input("Would you like to load your previous save state: ")
    if answer == "Yes":
        with open("users bet amount", "r") as openfile:
            Bet.user_amount = int(json.load(openfile))
    elif answer == "No":
        print("Creating New Save State!")
    else:
        print("Please Enter Yes or No")
        load_file()


# Deal out the cards to the player and dealer
def deal_cards():
    counter = 0
    card = ""
    while counter < 4:
        if counter > 1:
            card = random.choice(card_list)
            dealers_list.append(card)
            card_list.remove(card)
            counter += 1
        else:
            card = random.choice(card_list)
            users_list.append(card)
            card_list.remove(card)
            counter += 1
    print(users_list)

# User lost when dealer hit blackjack
def blackjack_loss():
    print("Dealer hit blackjack, You lose!")
    print("You now have: " + str(Bet.user_amount))
    Bet.save_bets(Bet.user_amount)
    play_again()


# Determines if someone has hit blackjack
def is_blackjack(hand):
    return set(hand) in [{"A", "10"}, {"A", "J"}, {"A", "Q"}, {"A", "K"}]


# Ends the game
def end_game():
    if users_total() > dealers_turn():
        print("Congrats, you win! Dealer had: " + str(dealers_total()))
        Bet.payout()
        Bet.save_bets(Bet.user_amount)
        play_again()
    elif users_total() == dealers_turn():
        print("Tie!")
        Bet.tie()
        Bet.save_bets(Bet.user_amount)
        play_again()
    else:
        print("You lose! Dealer had: " + str(dealers_total()))
        print("You now have: " + str(Bet.user_amount))
        Bet.save_bets(Bet.user_amount)
        play_again()


#Produces the users total
def users_total():
    user_total = 0
    for card in users_list:
        if card == "A":
            user_total += 11
        elif card in ["J", "Q", "K"]:
            user_total += 10
        else:
            user_total += int(card)

    if "A" in users_list:
        if user_total > 21:
            user_total -= 10

    return user_total


#Produces the dealers total
def dealers_total():
    value = 0
    num_aces = 0

    for card in dealers_list:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            value += 11
            num_aces += 1
        else:
            value += int(card)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Dealer makes its move based on the 17 rule
def dealers_turn():
    while dealers_total() < 17:
        card = random.choice(card_list)
        dealers_list.append(card)
        card_list.remove(card)

    if dealers_total() > 21:
        if "A" in dealers_list:
            dealers_list.remove("A")
            dealers_list.append("1")
        dealer_bust()

    return dealers_total()

#Dealer Busted, User wins
def dealer_bust():
    print("Dealer Busted! You Win! Dealer had: " + str(dealers_total()))
    Bet.payout()
    Bet.save_bets(Bet.user_amount)
    play_again()


#User loses the game due to going over 21
def lose_game():
    print("Bust!")
    print("You now have: " + str(Bet.user_amount))
    Bet.save_bets(Bet.user_amount)
    play_again()


#Determines if the user has bust
def is_bust():
    user_total = 0
    for card in users_list:
        if card == "A":
            user_total += 11
        elif card in ["J", "Q", "K"]:
            user_total += 10
        else:
            user_total += int(card)

    if "A" in users_list:
        if user_total > 21:
            user_total -= 10

    if user_total > 21:
        lose_game()


#Gives the user the option to stand or hit
def stand_and_hit(stand_or_hit):
    if stand_or_hit == "Hit":
        card = random.choice(card_list)
        users_list.append(card)
        card_list.remove(card)
        print(users_list)
        is_bust()
        stand_or_hit = input("Stand or Hit: ")
        stand_and_hit(stand_or_hit)
    elif stand_or_hit == "Stand":
        end_game()
    else:
        stand_or_hit = input("Please Enter Stand or Hit: ")
        stand_and_hit(stand_or_hit)

# Determines if the user wants to play again
def play_again():
    global card_list
    answer = input("Would you like to play again: ")
    if answer == "Yes":
        card_list += users_list + dealers_list
        users_list.clear()
        dealers_list.clear()
        initialize_again(answer)
    elif answer == "No":
        print("Sorry to hear that!")
        exit()
    else:
        print("Please Enter Yes or No!")
        play_again()

# Initializes the game not for the first time
def initialize_again(answer):
    if answer == "Yes":
        Bet.bet_amount()
        deal_cards()
        if is_blackjack(dealers_list):
            blackjack_loss()
        elif is_blackjack(users_list):
            Bet.blackjack_payout()
        stand_or_hit = input("Stand or Hit: ")
        stand_and_hit(stand_or_hit)
    elif answer == "No":
        print("Sorry to hear that!")
    else:
        start_button = input("Please Enter Yes or No: ")
        initialize(start_button)
