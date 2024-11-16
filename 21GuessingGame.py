def NearestMultiple(num):
    """
    Calculates the nearest multiple of 4 that is greater than or equal to the given number.
    """
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose1():
    """
    Prints a losing message and exits the game.
    """
    print("You Lose")
    print("Try Again")
    exit(0)


def check(xyz):
    """
    Checks if all numbers in the list `xyz` are consecutive.
    Returns True if they are consecutive, otherwise False.
    """
    for i in range(1, len(xyz)):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
    return True


def start1():
    """
    Manages the main game loop for the player's turns and the computer's responses.
    Allows the player to choose to go first ('F') or second ('S').
    """
    xyz = []  # List to track the sequence of numbers entered
    last = 0  # Tracks the last number in the sequence

    # Prompt the player to choose first or second turn
    print("Enter 'F' to take the first chance")
    print("Enter 'S' to take the second chance")
    chance = input("> ").strip().upper()

    # Check for valid choice
    if chance not in {'F', 'S'}:
        print("Wrong Choice")
        return

    # If the player chooses to go first
    if chance == 'F':
        while True:
            if last == 20:  # Game over condition
                lose1()

            # Player's turn
            print("Your Turn")
            print("How many numbers you wish to enter (1-3): ")

            # Take input for the number of values the player wants to add
            try:
                inp = int(input("> "))
                if inp <= 0 or inp > 3:
                    print("Wrong Input. Disqualified")
                    lose1()
            except ValueError:
                print("Invalid input. Exiting game.")
                lose1()

            # Calculate how many numbers the computer should add
            comp = 4 - inp
            print("Now enter the values")

            # Take the actual numbers from the player
            for _ in range(inp):
                try:
                    a = int(input("> "))
                    xyz.append(a)  # Append each number to the list
                except ValueError:
                    print("Invalid input. Exiting game.")
                    lose1()

            # Update `last` to the latest number in the list
            last = xyz[-1]

            # Check if the player's input is a consecutive sequence
            if check(xyz):
                if last == 21:
                    print("Congratulations! You win!")
                    exit(0)
                else:
                    # Computer's turn: add numbers to reach a multiple of 4
                    for j in range(1, comp + 1):
                        xyz.append(last + j)
                        print(f"Computer plays: {last + j}")
                    print("Order of the input after computer's turn is:")
                    print(xyz)
                    last = xyz[-1]  # Update `last` with the computer's last number
            else:
                # If the sequence is not consecutive, the player loses
                print("You did not input consecutive numbers.")
                lose1()

    # If the player chooses to go second
    elif chance == 'S':
        while True:
            # Computer's turn
            comp = NearestMultiple(last + 1)
            for i in range(last + 1, comp):
                xyz.append(i)
                print(f"Computer plays: {i}")

            # Update `last` to the latest number in the list
            last = xyz[-1]

            if last == 21:
                print("Congratulations! Computer wins!")
                lose1()

            # Player's turn
            print("Your Turn")
            print("How many numbers you wish to enter (1-3): ")

            try:
                inp = int(input("> "))
                if inp <= 0 or inp > 3:
                    print("Wrong Input. Disqualified")
                    lose1()
            except ValueError:
                print("Invalid input. Exiting game.")
                lose1()

            print("Now enter the values")
            for _ in range(inp):
                try:
                    a = int(input("> "))
                    xyz.append(a)
                except ValueError:
                    print("Invalid input. Exiting game.")
                    lose1()

            # Update `last` to the latest number in the list
            last = xyz[-1]

            # Check if the player's input is a consecutive sequence
            if not check(xyz):
                print("You did not input consecutive numbers.")
                lose1()

            if last == 21:
                print("Congratulations! You win!")
                exit(0)


def main():
    """
    Main game loop to prompt the player to start, continue, or quit the game.
    """
    while True:
        print("Player 2 is computer")
        print("Do you want to play? (y/n)")
        ans = input("> ").strip().lower()

        # Start the game if the player wants to play
        if ans == 'y':
            start1()
        elif ans == 'n':
            # Ask if the player wants to quit
            print("Do you want to quit? (y/n)")
            nex = input("> ").strip().lower()

            if nex == 'y':
                print("You are Quitting the Game")
                exit(0)
            elif nex == 'n':
                print("Continuing...")
            else:
                print("Wrong Choice")
        else:
            print("Invalid input. Try again.")


# Entry point for the program
if __name__ == "__main__":
    main()
