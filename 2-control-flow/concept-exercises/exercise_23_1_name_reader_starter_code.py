print("Welcome to the Name Reader!")
print()

name = input("Enter your name: > ")
first_letter = name[0]

if first_letter == "A":
    print("Names starting with A belong to natural leaders. People follow you without knowing why.")
elif first_letter == "B":
    print("Names starting with B belong to deeply loyal people. You never forget a friend.")
elif first_letter == "C":
    print("Names starting with C belong to the curious. You open every door just to see what is behind it.")
elif first_letter == "D":
    print("Names starting with D belong to dreamers. Your best ideas arrive right before you fall asleep.")
elif first_letter == "E":
    print("Names starting with E belong to the restless. Sitting still was never really your thing.")
elif first_letter == "F":
    print("Names starting with F belong to the fiercely honest. People always know where they stand with you.")
else:
    print("I do not have a reading for that letter yet. Your name keeps its secrets.")

print("The name reading is complete. Go forth.")
