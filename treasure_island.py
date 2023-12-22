print("Welcome to treasure Island. \n"
      "Your mission is to find the treasure.")
choice1 = input("You\'re at a crossroad, where do you want to go? Type 'left ' or 'right'. \n").lower()
if choice1 == "left":
    print("You are still alive")
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake."
                    " Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if choice2 == "wait":
        print('You are still alive.')
        choice3  = input("You arrive at the island unharmed."
                         "There is a house with 3 door. One red, One yellow and One blue\n").lower()
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "blue":
            print('You enter a room of beasts. Game over.')
        elif choice3 == "red":
            print("It's a room full of fire. Game Over")
        else:
            print("You choose a door that doesn't exist. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fel into a hole. Game Over.")

