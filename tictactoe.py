import random

# Tic-Tac-Toe board
board = [" " for _ in range(9)]


def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Function to check for a win
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to make the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Minimax algorithm for computer's move
def minimax(board, depth, maximizing_player):
    scores = {
        "X": 1,
        "O": -1,
        "Tie": 0,
    }

    if check_win(board, "X"):
        return scores["X"]
    if check_win(board, "O"):
        return scores["O"]
    if is_board_full(board):
        return scores["Tie"]

    if maximizing_player:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make the computer's move using Minimax
def computer_move(board):
    best_move = None
    best_eval = -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    player_turn = True
    while True:
        if not is_board_full(board):
            if player_turn:
                move = player_move(board)
                board[move] = "O"
            else:
                move = computer_move(board)
                board[move] = "X"

            print_board(board)

            if check_win(board, "O"):
                print("You win! Congratulations!")
                break
            elif check_win(board, "X"):
                print("Computer wins. Try again.")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            player_turn = not player_turn

        else:
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
