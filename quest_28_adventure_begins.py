def start_game():
    print("You stand at a crossroads. Do you go LEFT into the forest or RIGHT toward the mountains?")
    choice = input("> ").lower()

    if "left" in choice:
        forest_path()
    elif "right" in choice:
        mountain_path()
    else:
        print("Invalid choice. Try again.")
        start_game()

def forest_path():
    print("The trees are thick. You find a shiny sword! Do you PICK IT UP or LEAVE IT?")
    choice = input("> ").lower()
    
    if "pick" in choice:
        ending_hero()
    else:
        ending_lost()

def mountain_path():
    print("It's cold. You see a dragon sleeping. Do you SNEAK PAST or SHOUT?")
    choice = input("> ").lower()
    
    if "sneak" in choice:
        ending_hero()
    else:
        ending_crispy()

def ending_hero():
    print("Congratulations! You survived and became a legend.")

def ending_lost():
    print("You wandered the woods forever. Game Over.")

def ending_crispy():
    print("The dragon woke up... you are now toast. Game Over.")

start_game()