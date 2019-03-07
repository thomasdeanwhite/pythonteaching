from player import Player
import random

class JackiePlayer(Player):

    def __init__(self, player_num):
        self.player_num = player_num

    def make_move(self, connect_four):
        """move = random.randint(0, connect_four.grid_size[1]-1)

        while not connect_four.is_valid_move(move):
            move = random.randint(0, connect_four.grid_size[1]-1)

        board = connect_four.copy()
        board.make_move()"""

        connected_current_max = 0
        best_move = 0

        for i in range(connect_four.grid_size[1]):  # this is the length of the grid, so can change it if wanted, rather than hard coding
            move = i
            board = connect_four.copy()
            board.make_move(move)

            for cell in range(board.grid_size[0]):
                total = 0
                if board.board[-cell-1][i] == self.player_num+1:
                    total += 1
                else:
                    break
            if total > connected_current_max and connect_four.is_valid_move(move):
                connected_current_max = total
                best_move = move
        return best_move

    def get_name(self):
        return "Jackie"