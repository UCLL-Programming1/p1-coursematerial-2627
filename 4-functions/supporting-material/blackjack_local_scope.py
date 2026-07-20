from random import randrange

def deal_card(cards):
    random_index = randrange(len(cards))
    return cards.pop(random_index)

def get_card_value(card):
    if card == 'A':
        card_value = 1
    elif card == 'K' or card == 'Q' or card == 'J' or card == '10':
        card_value = 10
    else:
        card_value = int(card)
    return card_value

def main():
    cards = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

    print("Let's play blackjack!")

    card1 = deal_card(cards)
    card2 = deal_card(cards)
    print(f"Player hand is: {card1}, {card2}")

    hand_value = 0
    hand_value += get_card_value(card1)
    hand_value += get_card_value(card2)

    print("Player hand value is:", hand_value)
    choice = input("Do you want to (H)it or (S)tand? > ")

    while choice == 'H':
        new_card = deal_card(cards)

        print("Player got dealt:", new_card)
        hand_value += get_card_value(new_card)

        print("Player hand value is now:", hand_value)
        print() # for an extra empty line

        choice = input("Do you want to (H)it or (S)tand? > ")

    # after the while loop, we simply print the value of the player's hand
    print("")
    print("Player stood at:", hand_value)
main()
