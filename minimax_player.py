from player import Player

import math
import random

class MinimaxPlayer(Player):

    depth = 4

    def __init__(self, player_num):
        self.player_num = player_num + 1
        self.enemy_num = 2 if player_num == 0 else 1

    def make_move(self, connect_four):
        best = -math.inf
        moves = []
        for i in range(connect_four.grid_size[1]):
            if not connect_four.is_valid_move(i):
                continue
            board = connect_four.copy()
            board.make_move(i)
            r = self._make_move(board, 1, False)
            if r > best:
                moves = [i]
                best = r
            elif r == best:
                moves.append(i)
        return random.choice(moves)

    def _make_move(self, connect_four, depth, player):
        if depth > self.depth or not connect_four.playing:
            return self.rate_gamestate(connect_four, not player)

        fn = min
        value = math.inf

        if player:
            value = -math.inf
            fn = max
        for i in range(connect_four.grid_size[1]):
            if not connect_four.is_valid_move(i):
                continue
            board = connect_four.copy()

            board.make_move(i)

            value = fn(value, self._make_move(board, depth+1, not player))

        return value



    def rate_gamestate(self, board, player):
        r = board.max_in_row(self.player_num)
        r *= r
        if r >= 4:
            r *= 10000
        p = board.max_in_row(self.enemy_num)
        p *= p
        if p >= 4:
            p *= 10000
        return r-p

    def get_name(self):
        return "Minimax Player"
