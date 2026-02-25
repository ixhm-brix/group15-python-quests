# Quest 29: The Code Breaker

secret_code = 42
attempts = 3

for i in range(attempts):
    guess = int(input("Guess the secret code: "))
    
    if guess == secret_code:
        print("Correct! You cracked the code!")
        break
    else:
        remaining = attempts - (i + 1)
        if remaining > 0:
            print(f"Wrong! You have {remaining} attempts left.")
        else:
            print("Wrong! No more attempts. Game over!")