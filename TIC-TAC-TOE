import random

board = [" "] * 9

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

while True:
    show_board()

    # Human move
    move = int(input("Enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    winner = check_winner()
    if winner:
        show_board()
        print("Result:", winner)
        break

    # Robot move
    empty = [i for i in range(9) if board[i] == " "]
    robot_move = random.choice(empty)
    board[robot_move] = "O"

    print("Robot chose:", robot_move + 1)

    winner = check_winner()
    if winner:
        show_board()
        print("Result:", winner)
        break
