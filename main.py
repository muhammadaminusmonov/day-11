import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []


def check_score():
    user_total_score = sum(user_cards)
    dealer_total_score = sum(dealer_cards)

    if (user_total_score == 21 and dealer_total_score == 21) or (user_total_score > 21 and dealer_total_score > 21):
        print("It is draw")
    elif user_total_score == 21 or dealer_total_score > 21:
        print("How lucky you won!")
    elif dealer_total_score == 21 or user_total_score > 21:
        print("You lost")
    else:
        return

    game_continue()


def final_check():
    check_score()


def game_continue():
    game = input("Do you want to play blackjack? y/n: ")
    if game == "y":
        print(art.logo)

        for _ in range(0, 2):
            user_cards.append(rand_card())
        print(f"Your cards are {user_cards} and total is {sum(user_cards)}")

        dealer_cards.append(rand_card())
        print(f"Dealer's first card is {dealer_cards}")

        check_score()

    else:
        print("Hope you to play the game next time")


def rand_card():
    card = random.choice(cards)
