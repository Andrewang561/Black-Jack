import random
import Bet

card_list = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3",
    "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7"
    , "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J"
    , "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

dealers_list = []
users_list = []



# Initialize the game
def initialize(start_button):
    if start_button == "yes":
        Bet.bet_amount()
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
        if is_blackjack(dealers_list):
            blackjack_loss()
        elif is_blackjack(users_list):
            Bet.blackjack_payout()
        stand_or_hit = input("Stand or Hit: ")
        stand_and_hit(stand_or_hit)
    else:
        print("Sorry to hear that!")

# User lost when dealer hit blackjack
def blackjack_loss():
    print("Dealer hit blackjack, You lose!")
    print("You now have: " + str(Bet.user_amount))
    play_again()


# Determines if someone has hit blackjack
def is_blackjack(hand):
    return set(hand) in [{"A", "10"}, {"A", "J"}, {"A", "Q"}, {"A", "K"}]


# Ends the game
def end_game():
    if users_total() > dealers_total():
        print("Congrats, you win!")
        Bet.payout()
        play_again()
    else:
        print("You lose!")
        print("You now have: " + str(Bet.user_amount))
        play_again()


#Produces the users total
def users_total():
    user_total = 0
    for n in users_list:
        if n == "A":
            value = input("Ace is 1 or 11: ")
            user_total += int(value)
        elif n == "J" or n == "Q" or n == "K":
            user_total += 10
        else:
            user_total += int(n)
    return user_total


#Produces the dealers total
def dealers_total():
    dealer_total = 0
    for n in dealers_list:
        if n == "A":
            dealer_total += 11
        elif n == "J" or n == "Q" or n == "K":
            dealer_total += 10
        else:
            dealer_total += int(n)
    print("Dealer's Total: " + str(dealer_total))
    return dealer_total


#User loses the game due to going over 21
def lose_game():
    print("Bust!")
    play_again()


#Determines if the user has bust
def is_bust():
    user_total = 0
    for n in users_list:
        if n == "A":
            value = input("Ace is 1 or 11: ")
            user_total += int(value)
        elif n == "J" or n == "Q" or n == "K":
            user_total += 10
        else:
            user_total += int(n)
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
    else:
        end_game()

# Determines if the user wants to play again
def play_again():
    global card_list
    answer = input("Would you like to play again: ")
    if answer == "yes":
        card_list += users_list + dealers_list
        users_list.clear()
        dealers_list.clear()
        initialize(answer)
    else:
        print("Sorry to hear that!")
