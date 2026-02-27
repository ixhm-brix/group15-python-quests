print("Welcome to the Mystery Forest ")


path = input("Do you go 'left' or 'right'? ")

if path == "left":

    action = input("You see a river. Do you 'swim' or 'wait'? ")
    
    if action == "swim":
        print("You found a bag of gold in the water! You win!")
    else:
        print("You waited too long and a bear found you. Game over.")

else:

    print("You walked into a dark cave and got lost!")