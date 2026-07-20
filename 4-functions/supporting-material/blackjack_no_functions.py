from random import randrange # need to import randrange

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

print("Let's play blackjack!")

random_card_index = randrange(len(deck))
card1 = deck.pop(random_card_index)

random_card_index = randrange(len(deck))
card2 = deck.pop(random_card_index)

print(f"Player hand is: {card1}, {card2}")

hand_value = 0

if card1 == 'A':
    card_value = 1
elif card1 == 'K' or card1 == 'Q' or card1 == 'J' or card1 == '10':
    card_value = 10
else:
    card_value = int(card1)
hand_value += card_value

if card2 == 'A':
    card_value = 1
elif card2 == 'K' or card2 == 'Q' or card2 == 'J' or card2 == '10':
    card_value = 10
else:
    card_value = int(card1)
hand_value += card_value

print("Player hand value is:", hand_value)
choice = input("Do you want to (H)it or (S)tand? > ")

while choice == 'H':
    random_card_index = randrange(len(deck))
    new_card = deck.pop(random_card_index)

    print("Player got dealt:", new_card)

    if new_card == 'A':
        card_value = 1
    elif new_card == 'K' or new_card == 'Q' or new_card == 'J' or new_card == '10':
        card_value = 10
    else:
        card_value = int(new_card)
    hand_value += card_value

    print("Player hand value is now:", hand_value)
    print() # for an extra empty line

    choice = input("Do you want to (H)it or (S)tand? > ")

# after the while loop, we simply print the value of the player's hand
print("")
print("Player stood at:", hand_value)
