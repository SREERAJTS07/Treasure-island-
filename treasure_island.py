print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# Asking for user input for the first decision
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    print("You are still alive.")
    # Asking for user input for the second decision
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if choice2 == "wait":
        print("You are still alive.")
        # Asking for user input for the third decision
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors: one red, one yellow, and one blue. "
                        "Which door do you choose? ").lower()

        if choice3 == "yellow":
            print("Congratulations! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
