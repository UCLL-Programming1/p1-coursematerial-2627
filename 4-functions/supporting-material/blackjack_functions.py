from random import randrange # need to import randrange

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

def get_card_value(card):
    if card == 'A':
        card_value = 1
    elif card == 'K' or card == 'Q' or card == 'J' or card == '10':
        card_value = 10
    else:
        card_value = int(card)
    return card_value

def deal_card():
    random_card_index = randrange(len(deck))
    card = deck.pop(random_card_index)
    return card # don't forget the return!

print("Let's play blackjack!")

card1 = deal_card()
card2 = deal_card()

print(f"Player hand is: {card1}, {card2}")

hand_value = 0

hand_value += get_card_value(card1)
hand_value += get_card_value(card2)

print("Player hand value is:", hand_value)
choice = input("Do you want to (H)it or (S)tand? > ")

while choice == 'H':
    new_card = deal_card()

    print("Player got dealt:", new_card)
    hand_value += get_card_value(new_card)

    print("Player hand value is now:", hand_value)
    print() # for an extra empty line

    choice = input("Do you want to (H)it or (S)tand? > ")

# after the while loop, we simply print the value of the player's hand
print("")
print("Player stood at:", hand_value)
