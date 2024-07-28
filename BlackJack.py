import random

card_list = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3"
    , "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7"
    , "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J"
    , "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

dealers_list = []
users_list = []
start_button = input("Would you like to play blackjack: ")

#Intialize the game
def initialize(start_button):
    if start_button == "yes":
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
    else:
        print("Sorry to hear that!")

initialize(start_button)
print(users_list)

stand_or_hit = input("Stand or Hit: ")

#Ends the game
def end_game():
    if users_total() > dealers_total():
        print("Congrats, you win!")
    else:
        print("You lose!")

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
    exit()

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

stand_and_hit(stand_or_hit)












