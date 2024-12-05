import random # Add library to randomly choose which player to start with


def display_board(board): # Display function of the current state of the game board
    print("╔══════╦══════╦══════╗") # Limits the top of the tray
    for i in range(0, 9, 3): # for loop that iterates over indices 0, 3, and 6 (not 3) to display 3 lines
        print(f"║ {board[i]} ║ {board[i+1]} ║ {board[i+2]} ║") # Each line displays 3 consecutive elements of the parameter panel
        if i == 0 or i == 3:
            print("╠══════╬══════╬══════╣") # Condition that prints a separator after line 0 and line 3
    print("╚══════╩══════╩══════╝") # Limits the bottom of the tray


def player_turn(board, player): # Function that manages the player's turn (selects 1 cell and updates the board) and takes 2 parameters
    valid_choice = True # Variable used to determine if the player's choice is valid
    while valid_choice: # Loop that continues to execute as long as the selection is invalid
        try: # Testing a block of code
            choice = int(input(f"Player {player}, choose a square between 1 and 9 : ")) - 1 # Requires an input (converted to an integer) from the player and subtracts 1 to make it fun (since list indices start at 0)
            if choice < 0 or choice > 8 or board[choice] != "    ":
            # Checks if the selection is < to 0, > to 8, or if the field is not empty
                print("Invalid choice, try again : ") # Display a message
            else: # If none of the above conditions is true, this block is executed
                board[choice] = player # Refreshes the board by writing the player's symbol on the selected square
                valid_choice = False # Ends the loop by making the while valid_choice condition false
        except ValueError: # Catch an error if the user enters something that is not a number, to avoid a bug
            print("Enter a valid number : ") # Display a message


def ai_turn(board, player): # Artificial intelligence tour function


    for i in range(9): # The loop covers all 9 squares on the board
        if board[i] == "    ":
            board[i] = player # If a square is empty, it is temporarily played by the player
            if check_victory(board, player):
                return # If this action results in a win, the function stops immediately
            board[i] = "    " # Otherwise, the move is canceled and the program continues testing other options
    # 1°) Checks if the AI can win immediately, and if so, the AI plays this square
    
    if board[4] == "    ":
        board[4] = player
        return
    # 2°) If the central square is free, the AI takes it


    for i in [0, 2, 6, 8]:
        if board[i] == "    ":
            board[i] = player
            return
    # 3°) If a corner is free, the AI chooses it
    
    for i in range(9):
        if board[i] == "    ":
            board[i] = player
            return
    # 4°) If none of these options is possible, the AI will choose a free square


def check_victory(board, player): # Function that checks if a player has won and takes 2 parameters
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # List of all possible winning combinations (3 rows, 3 columns, 2 diagonals)
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    # Scans each winning combination and checks if all cells in the combination contain the player's symbol (if so, returns True)
    return False # If no winning combination is found, returns False


def play(): # Function manages all game logic
    board = ["    " for i in range(9)] # Creates a board represented by a list of 9 empty cells
    mode = input('Choose mode : "1" for Player vs Player or "2" for Player vs AI : ')
    # Prompts the player to select the game mode
    
    current_player = random.choice([" 🦊 ", " 🐸 "]) # Random selection of the first player
    print(f"The first player is randomly chosen to be Player {current_player}.")
    
    for turn in range(9):  # Loop that iterates a maximum of 9 loops
        display_board(board)  # Shows the current state of the board
        
        if mode == "1":
            player_turn(board, current_player)
        # If the mode is Player vs. Player, call the player to play
        
        elif mode == "2" and current_player == " 🦊 ":
            player_turn(board, current_player)
        # When it's "🦊's" turn in mode 2, call the player to play


        else:
            ai_turn(board, current_player)
        # Otherwise, call the AI to play


        if check_victory(board, current_player):
            display_board(board)
            print(f"Congratulations ! Player {current_player} has won !")
            return
        # After each round, check to see if the current player has won. If so, display a message and end the game
        
        if current_player == " 🦊 ":
            current_player = " 🐸 "
        else:
            current_player = " 🦊 "
        # Change player for next round ("🦊" becomes "🐸" and vice versa)
    
    display_board(board)
    print("It's a draw !")
    # If no player wins after 9 rounds, displays the final board and a message


play() # Calls the play() function to start the game
