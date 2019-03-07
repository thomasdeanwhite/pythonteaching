from player import Player
import random

class RandomPlayer(Player):

    def __init__(self, player_num):
        self.player_num = player_num

    def make_move(self, connect_four):
        move = random.randint(0, connect_four.grid_size[1]-1)  #  choose a  random no btw 0 and the size of the board

        while not connect_four.is_valid_move(move):
            move = random.randint(0, connect_four.grid_size[1]-1)
        return move

    def get_name(self):
        return "Random Player"

# function returns a number for which column the player wants to drop the counter in