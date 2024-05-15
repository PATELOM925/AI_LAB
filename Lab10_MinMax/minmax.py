class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

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

def minimax_with_path(board, depth, maximizing_player, alpha, beta):
    if board.is_game_over() or depth == 0:
        if board.check_winner() == 'X':
            return -10 + depth, None, []
        elif board.check_winner() == 'O':
            return 10 - depth, None, []
        else:
            return 0, None, []

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        best_path = []
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval, _, path = minimax_with_path(board, depth - 1, False, alpha, beta)
            board.undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
                best_path = path
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move, [(move, 'O')] + best_path

    else:
        min_eval = float('inf')
        best_move = None
        best_path = []
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval, _, path = minimax_with_path(board, depth - 1, True, alpha, beta)
            board.undo_move(move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
                best_path = path
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move, [(move, 'X')] + best_path


def play_tic_tac_toe():
    board = TicTacToe()
    current_player = 'X'

    while not board.is_game_over():
        if current_player == 'X':
            _, move = minimax_with_path(board, 9, True, float('-inf'), float('inf'))
        else:
            _, move = minimax_with_path(board, 9, False, float('-inf'), float('inf'))

        if move:
            board.make_move(move, current_player)
            board.print_board()
            print()
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("It's a tie!")
            break

    winner = board.check_winner()
    if winner:
        print(f"Player {winner} wins!")
    elif board.is_board_full():
        print("It's a tie!")

play_tic_tac_toe()
