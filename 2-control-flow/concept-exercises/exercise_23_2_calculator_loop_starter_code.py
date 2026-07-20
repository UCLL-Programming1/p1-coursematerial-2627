operation = input("Provide the symbol of the operation you want to perform: > ")
first_number = float(input("Provide your first number: > "))
second_number = float(input("Provide your second number: > "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "/":
    result = first_number / second_number
else:
    result = first_number * second_number
print("Your resulting value is " + str(result) + ".")
