#minmax Tictac toe 
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]


    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 6)

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_game_over(self):
        return self.check_winner() or self.is_board_full()

    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def make_move(self, move, player):
        if self.board[move[0]][move[1]] == ' ':
            self.board[move[0]][move[1]] = player
            return True
        return False

    def undo_move(self, move):
        self.board[move[0]][move[1]] = ' '

def minimax(board, depth, maximizing_player):
    if board.is_game_over() or depth == 0:
        if board.check_winner() == 'X':
            return -10 + depth, None
        elif board.check_winner() == 'O':
            return 10 - depth, None
        else:
            return 0, None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval, _ = minimax(board, depth - 1, False)
            board.undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval, _ = minimax(board, depth - 1, True)
            board.undo_move(move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

def play_tic_tac_toe():
    board = TicTacToe()
    current_player = 'X'

    while not board.is_game_over():
        board.print_board()
        print()

        if current_player == 'X':  # User's turn
            while True:
                try:
                    print("Your Turn")
                    row = int(input("Place in row (1-3): ")) - 1
                    col = int(input("Place in column (1-3): ")) - 1
                    if 0 <= row <= 2 and 0 <= col <= 2 and board.board[row][col] == ' ':
                        break
                    else:
                        print("Invalid !! Try again.")
                except ValueError:
                    print("Invalid. ValueError. Try again.")
            
            board.make_move((row, col), current_player)

        else:  # AI's turn
            print("AI's Turn")
            _, move = minimax(board, 9, True)
            board.make_move(move, current_player)

        current_player = 'X' if current_player == 'O' else 'O'

    board.print_board()
    print()

    winner = board.check_winner()
    if winner:
        print(f"Player {winner} wins!")
    elif board.is_board_full():
        print("It's a tie!")

play_tic_tac_toe()