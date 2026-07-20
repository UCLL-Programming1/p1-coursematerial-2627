from random import randrange

def create_deck():
    suits = ["H", "D", "C", "S"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit + rank)
    return deck

def deal_card(deck):
    random_index = randrange(len(deck))
    return deck.pop(random_index)

def deal_cards(deck, number):
    cards = []
    for _ in range(number):
        cards.append(deal_card(deck))
    return cards

def is_playable(card, top_card, top_suit):
    return card[0] == top_suit or card[1:] == top_card[1:] or card[1:] == "8"

def play_turn(player_cards, deck, discard_pile, current_suit):
    top_card = discard_pile[-1]

    finish_turn = False
    while not finish_turn:
        print("Top card:", top_card)
        print("Top suit:", current_suit)
        print("Your hand:", player_cards)
        move = input("Play card or draw (D): > ").upper()

        if move == 'D':
            finish_turn = True
            print("Player drew a card")
            player_cards.append(deal_card(deck))

            # Put the cards of the discard pile back into the deck (except the last one)
            if len(deck) == 0:
                while len(discard_pile) > 1:
                    deck.append(discard_pile.pop(0)) # no need to shuffle since we draw at random.

        elif move not in player_cards:
            print("You don't have this card in your hand, play again")

        elif not is_playable(move, top_card, current_suit):
            print("The card you want to play doesn't match the suit nor rank of the top card")

        else:
            finish_turn = True
            player_cards.remove(move)

            # 8 changes suit
            if move[1] == '8':
                suit = input("Choose suit (H D C S): > ").upper()
                current_suit = suit
            else:
                current_suit = move[0]

            discard_pile.append(move)

        print()

    return current_suit

def main():
    # Create deck
    deck = create_deck()

    player_1_cards = deal_cards(deck, 5)
    player_2_cards = deal_cards(deck, 5)

    # Start discard pile
    discard_pile = []
    discard_pile.append(deal_card(deck))
    current_suit = discard_pile[-1][0]

    game_over = False
    while not game_over:
        print("Player 1 Turn!")
        current_suit = play_turn(player_1_cards, deck, discard_pile, current_suit)
        if not player_1_cards:
            print("Player 1 wins!")
            game_over = True
        else:
            print("Player 2 Turn!")
            current_suit = play_turn(player_2_cards, deck, discard_pile, current_suit)
            if not player_2_cards:
                print("Player 2 wins!")
                game_over = True

main()
