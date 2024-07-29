import BlackJack


def main():
    start_button = input("Would you like to play blackjack: ")
    BlackJack.initialize(start_button)
    print(BlackJack.users_list)
    stand_or_hit = input("Stand or Hit: ")
    BlackJack.stand_and_hit(stand_or_hit)


main()
