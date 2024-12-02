def check_victory(board, player):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False