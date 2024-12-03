def display_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i == 0 or i == 3:
            print("---+---+---")
