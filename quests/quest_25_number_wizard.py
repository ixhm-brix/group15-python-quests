secret_number = 7  
guess = 0

print("I am the Number Wizard! Guess my secret number (1-10).")


while guess != secret_number:
    guess = int(input("What is your guess? "))
    
    if guess < secret_number:
        print("Too low! Try a bigger spell.")
    elif guess > secret_number:
        print("Too high! Scale it back.")
    else:
        print("🎉 Correct! You are a true Number Wizard.")