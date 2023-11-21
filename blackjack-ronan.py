import random
import os
from art import logo

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Methods
"""Deals cards to the arguments"""
def deal_card(participant):
    draw_card = random.choice(cards)
    participant.append(draw_card)

"""Shows the hands of the participants and takes a number to assess whether it is the computer or player"""
def show_hand(participant, num):
    str_participant = ""
    for card in participant:
        str_participant += f"{card}, "
    if num == 1:
        print(f"Your hand: {str_participant} \nYour total: {sum(participant)}")
    else:
        print(f"\nDealer hand: {str_participant} \nDealer hand total: {sum(participant)}")

def change_ace(participant, num):
    for position in range(len(participant)):
        if participant[position] == 11:
            participant[position] = 1
            show_hand(participant, num)

def hit_stand_choice(participant):
    repeat = True
    game_over = False
    while repeat:
        print("\nWould you like to hit or stand?")
        hit_stand = input("Enter 'hit' or 'stand': ").lower()
        if hit_stand == "hit":
            deal_card(participant)
            if sum(participant) > 21:
                change_ace(participant, 1)
                if sum(participant) > 21:
                    show_hand(participant, 1)
                    print("Bust! Your hand is over 21.")
                    repeat = False
                    game_over = True
                    user_restart()
            else:
                show_hand(participant, 1)
        else:
            repeat = False
    return game_over

def computer_count(computer):
    if sum(computer) < 17:
        while sum(computer) < 17:
            deal_card(computer)
    elif sum(computer) > 21:
        change_ace(computer, 2)
    return sum(computer)

def compare_hands(p_sum, c_sum, player, computer):
    show_hand(player, 1)
    show_hand(computer, 2)
    if p_sum <= 21 and c_sum > 21:
        print("\nYou win.")
    elif p_sum == c_sum:
        blackjack()    
    elif p_sum > c_sum:
        print("\nYou win.")
    else:
        print("\nThe dealer wins.")

def user_restart():
    go_again = input("\nEnter 'Y' to start again or 'N' to quit: ").lower()
    if go_again == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
        
def blackjack():
    player_cards = []
    computer_cards = []
    print(logo)
    # Deal cards to computer and player 
    # Deals cards until computer and player each have 2
    while len(player_cards) <= 1:
        deal_card(player_cards)
    while len(computer_cards) <= 1:
        deal_card(computer_cards)

    # Show player cards and second computer card
    show_hand(player_cards, 1)
    print(f"Dealer hand: X, {computer_cards[1]}")

    # Player decides to hit or stand
    game_over = hit_stand_choice(player_cards)

    # Sum pools for player and computer
    if not game_over:
        player_sum = sum(player_cards)
        computer_sum = computer_count(computer_cards)

        compare_hands(player_sum, computer_sum, player_cards, computer_cards)
    user_restart()
        
blackjack()