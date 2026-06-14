import math

# Create empty board
board = [' ' for _ in range(9)]


def print_board():
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")


def print_positions():
    print("\nBoard Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(player):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True

    return False


def is_draw():
    return ' ' not in board


def minimax(is_maximizing):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score


def ai_move():

    best_score = -math.inf
    best_move = None

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'


def human_move():

    while True:

        try:
            position = int(input("Enter your move (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position] != ' ':
                print("Position already occupied.")
                continue

            board[position] = 'X'
            break

        except ValueError:
            print("Invalid input. Enter a number.")


def play_game():

    print("=" * 35)
    print("      TIC TAC TOE AI")
    print("=" * 35)

    print("\nYou = X")
    print("AI  = O")

    print_positions()

    while True:

        print_board()

        human_move()

        if check_winner('X'):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 Match Draw!")
            break

        print("AI is thinking...")
        ai_move()

        if check_winner('O'):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 Match Draw!")
            break


if __name__ == "__main__":
    play_game()