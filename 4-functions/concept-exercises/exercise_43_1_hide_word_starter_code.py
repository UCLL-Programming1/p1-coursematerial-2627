word = input("Enter a word to hide: > ")
shown_letters = input("Enter the letters of the word that need to be shown: > ")

hidden_word = ""
index = 0
while index < len(word):
    if word[index] in shown_letters:
        hidden_word += word[index]
    else:
        hidden_word += "*"
    index += 1

print(f"The hidden word is: {hidden_word}")
