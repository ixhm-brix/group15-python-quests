#!/usr/bin/python3
def ask_for_age():
    user_age = int(input("Enter your age: "))
    return user_age

def can_they_vote(user_age):
    if user_age >= 20:
        print("Allowed to vote")
    else:
        print("Not allowed to vote")

user_age = ask_for_age()
can_they_vote(user_age)
