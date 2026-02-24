#!/usr/bin/python3

secret_number = 9
answer_input = int(input("Enter the secret number: "))

while answer_input != secret_number:
    print("The answer is wrong")
    print("Hint: The answer is an odd number and is in the range 1-10.")
    answer_input = int(input("Enter the secret number: "))
else:
    print("Congratulations!! The answer is correct")
