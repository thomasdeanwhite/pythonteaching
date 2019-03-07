from player import Player
import random

class BadPlayer(Player):

    def __init__(self, player_num):
        self.player_num = player_num

    def make_move(self, connect_four):
        move = 0

        while not connect_four.is_valid_move(move):
            move += 1

        board = connect_four.copy()
        board.make_move(2)

        if board.max_in_row(self.player_num+1) > 1:
            return 2
        return move

    def get_name(self):
        return "Bad Player"