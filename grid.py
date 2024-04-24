# Amanda Hinnerichs
# 04/19/2024
# Assignment: grid.py
# Description: a simple game played on a 20 x 20 dot grid where user input makes the
# the letter "x" move up, down, left, or right on the grid.

grid_size = 20  #size of the grid (20x20)
x, y = 0, 0  # Initial position of the player
#====================================================================================

                    # Function to print the grid with the player's current position
def print_grid(x, y):
    for row in range(grid_size):
        for col in range(grid_size):
            if col == x and row == y:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()  # Move to the next line after each row


                    # Main game loop
def main():
    global x, y
    print_grid(x, y)  # Display the initial grid

    while True:
        move = input("Move your player (w=up, s=down, a=left, d=right, quit=exit game): ").lower()

        if move == "quit":
            print("Game ended.")
            break
        elif move == "w" and y > 0:
            y -= 1  # Move up
        elif move == "s" and y < grid_size - 1:
            y += 1  # Move down
        elif move == "a" and x > 0:
            x -= 1  # Move left
        elif move == "d" and x < grid_size - 1:
            x += 1  # Move right
        else:
            print("Invalid move. Please use w, a, s, d or quit.")

        print_grid(x, y)  # Update and display the grid with the new position

#===========================================================================================
                    # Run the game
if __name__ == "__main__":
    main()