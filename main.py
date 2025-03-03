# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# def player(cards):
#     player1 = []
#     player1.append(random.choice(cards))
#     player1.append(random.choice(cards))
#     print(player1)
#
#     total = sum(player1)
#     print(total)
#
#     while total < 21:
#         request_more = input("Would you like another card? Y or N").lower()
#         if request_more == "y":
#             player1.append(random.choice(cards))
#             total = sum(player1)  # Update total after adding a card
#             print(player1)
#             print(total)
#
#             # Adjust for Ace (11 -> 1) if total > 21
#             if total > 21 and 11 in player1:
#                 player1[player1.index(11)] = 1
#                 total = sum(player1)
#
#             if total > 21:
#                 print("Busted!")
#                 break
#
#         elif request_more == "n":
#             print("Final total:", total)
#             break
#
#
# def dealer(cards):
#     dealer1 = []
#     dealer1.append(random.choice(cards))
#     dealer1.append(random.choice(cards))
#     total = (sum(dealer1))
#     while total < 17:
#         dealer1.append(random.choice(cards))
#         total = (sum(dealer1))
#     print(f"Dealer's final total, {total}")
#     return total
#
# def check_winner():
#     if player(cards) > dealer(cards) and player(cards) <= 21:
#         print(f"Player has won {player(cards)}")
#     else:
#         print(f"Dealer has won {dealer(cards)}")
#
# print(player(cards))
# print(dealer(cards))
# print(check_winner())


import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


