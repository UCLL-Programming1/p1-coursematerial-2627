print("Let's see who has the highest card!")
card_1 = input("Player 1, enter your card: > ")
card_2 = input("Player 2, enter your card: > ")

if card_1 == "Jack":
    card_1 = "11"
if card_2 == "Jack":
    card_2 = "11"

if card_1 == "Queen":
    card_1 = "12"
if card_2 == "Queen":
    card_2 = "12"

if card_1 == "King":
    card_1 = "13"
if card_2 == "King":
    card_2 = "13"

if card_1 > card_2:
    print("Player 1 has the highest card!")
elif card_1 < card_2:
    print("Player 2 has the highest card!")
else:
    print("Both players are holding the same value card!")
