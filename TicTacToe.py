"""
Developer: Sami Nachwati
Purpose: this program runs the basic elements of the famous Tic-Tac-Toe game
Language: English
Programming Language: Python
"""

# sets the display of the grid with nested lists
grid = [[" "], [" "], [" "]]
grid2 = [[" "], [" "], [" "]]
grid3 = [[" "], [" "], [" "]]

# stores 3 grids into a variable called total_grid
total_grid = f"{grid}\n\n{grid2}\n\n{grid3}"

# displays the grid
print(total_grid)

# a dictionary that sets numbered values to coordinate values
grid_Coordinates = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 0),
    5: (1, 0),
    6: (2, 0),
    7: (0, 0),
    8: (1, 0),
    9: (2, 0)
}

# a count used to keep track of how many turns there are
c = 0

# sets the game to True, which is on
game = True

# while the game is on
while game:

    # ask the user for their choice between x and o
    user_choice = input("Enter your choice (x or o): ").lower()

    # assuming the user does not enter x or o, ask them again
    if user_choice != "x" and user_choice != "o":
        continue

    # if the user does enter a value of x or o, ask them where they want to place it on the grid
    elif user_choice == "x" or user_choice == "o":
        user_turn = int(input("Enter a number for your turn based on the numbered grid (1-3 first row, 4-6 second row, "
                              "7-9 last row): "))

        # if the user enters a value between 1 and 3 inclusive, then, the user's value is in the first row
        if 3 >= user_turn >= 1:
            # assign 2 variables to the tuple of the 2 values for the grid
            # assign the value in the grid to the user's symbol
            grid_x, grid_y = grid_Coordinates[user_turn]
            grid[grid_x][grid_y] = user_choice

        # if the user enters a value between 4 and 6 inclusive, then, the user's value is in the second row
        elif 6 >= user_turn >= 4:

            # assign 2 variables to the tuple of the 2 values for the grid
            # assign the value in the grid to the user's symbol
            grid_x2, grid_y2 = grid_Coordinates[user_turn]
            grid2[grid_x2][grid_y2] = user_choice

        # if the user enters a value between 7 and 9 inclusive, then, the user's value is in the third row
        elif 9 >= user_turn >= 7:

            # assign 2 variables to the tuple of the 2 values for the grid
            # assign the value in the grid to the user's symbol
            grid_x3, grid_y3 = grid_Coordinates[user_turn]
            grid3[grid_x3][grid_y3] = user_choice
    # after each condition, update the total grid
    total_grid = f"{grid}\n\n{grid2}\n\n{grid3}"

    # keep on incrementing the count as to keep track of the amount of turns that went by
    c += 1

    # assuming the user(s) have entered values more than 9 times, then, the grid has to be
    # full and no one won, so, it is a tie
    if c >= 9 and game:
        # display that it is a tie
        print("Tie!")
        # end the game
        game = False

    # otherwise, display the updated grid
    print(total_grid)

    # check the winning conditions for x, if x wins, display x won and quit the program
    if (grid[0][0] == "x" and grid[1][0] == "x" and grid[2][0] == "x") or \
            (grid2[0][0] == "x" and grid2[1][0] == "x" and grid2[2][0] == "x") \
            or (grid3[0][0] == "x" and grid3[1][0] == "x" and grid3[2][0] == "x") \
            or (grid[0][0] == "x" and grid2[0][0] == "x" and grid3[0][0] == "x") \
            or (grid[1][0] == "x" and grid2[1][0] == "x" and grid3[1][0] == "x") \
            or (grid[2][0] == "x" and grid2[2][0] == "x" and grid3[2][0] == "x") \
            or (grid[0][0] == "x" and grid2[1][0] == "x" and grid3[2][0] == "x") \
            or (grid[2][0] == "x" and grid2[1][0] == "x" and grid3[0][0] == "x"):
        print('X wins!')
        game = False

    # check the winning conditions for o, if o wins, display o won and quit the program
    if (grid[0][0] == "o" and grid[1][0] == "o" and grid[2][0] == "o") or \
            (grid2[0][0] == "o" and grid2[1][0] == "o" and grid2[2][0] == "o") \
            or (grid3[0][0] == "o" and grid3[1][0] == "o" and grid3[2][0] == "o") \
            or (grid[0][0] == "o" and grid2[0][0] == "o" and grid3[0][0] == "o") \
            or (grid[1][0] == "o" and grid2[1][0] == "o" and grid3[1][0] == "o") \
            or (grid[2][0] == "o" and grid2[2][0] == "o" and grid3[2][0] == "o") \
            or (grid[0][0] == "o" and grid2[1][0] == "o" and grid3[2][0] == "o") \
            or (grid[2][0] == "o" and grid2[1][0] == "o" and grid3[0][0] == "o"):
        print('O wins!')
        game = False

    # end of code
