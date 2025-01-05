from colorama import Fore, Style


def minimax(board, depth, is_maximizing):
    """Implements the minimax algorithm to calculate the optimal move."""
    winner = check_winner(board)
    if winner == "X":  # X wins
        return -10 + depth
    if winner == "O":  # O wins
        return 10 - depth
    if winner == "Draw":  # Draw
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(best_score, score)
        return best_score


def print_board(board):
    """Prints the current state of the board with colors."""
    for row in board:
        colored_row = [
            f"{Fore.RED}X{Style.RESET_ALL}" if cell == "X" else
            f"{Fore.GREEN}O{Style.RESET_ALL}" if cell == "O" else
            " "
            for cell in row
        ]
        print(" | ".join(colored_row))
        print("-" * 9)


def check_winner(board):
    """Checks if there's a winner or a draw."""
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for draw (no empty spaces left)
    for row in board:
        if " " in row:
            return None
    return "Draw"


def ai_move(board):
    """Calculates the best move for the AI using the minimax algorithm."""
    best_score = float("-inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def tic_tac_toe1():
    """Main game loop."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player input
        try:
            move = input(
                f"Player {current_player}, enter your move (row and column: 1 1): ")
            row, col = map(int, move.split())
            row -= 1
            col -= 1

            # Validate the move
            if row not in range(3) or col not in range(3) or board[row][col] != " ":
                print("Invalid move. Try again.")
                continue

            # Make the move
            board[row][col] = current_player

            # Print the updated board
            print_board(board)

            # Check for a winner or draw
            result = check_winner(board)
            if result == "Draw":
                print("It's a draw!")
                break
            elif result:
                print(f"Player {result} wins!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Enter row and column numbers separated by a space.")


def tic_tac_toe():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == "X":  # Human player
            try:
                move = input(
                    f"Player {current_player}, enter your move (row and column: 1 1): ")
                row, col = map(int, move.split())
                row -= 1
                col -= 1

                if row not in range(3) or col not in range(3) or board[row][col] != " ":
                    print("Invalid move. Try again.")
                    continue

                board[row][col] = current_player
            except ValueError:
                print(
                    "Invalid input. Enter row and column numbers separated by a space.")
                continue
        else:  # AI's turn
            print("AI is making a move...")
            row, col = ai_move(board)
            board[row][col] = current_player

        print_board(board)

        result = check_winner(board)
        if result == "Draw":
            print("It's a draw!")
            break
        elif result:
            print(f"Player {result} wins!")
            break

        current_player = "O" if current_player == "X" else "X"


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
