number = int(input("Game master, enter a number: > "))
guess = int(input("Player, guess the number: > "))
while guess != number:
    if guess > number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    print("Try again!")
    guess = int(input("Player, guess the number: > "))
print("You guessed correctly!")
