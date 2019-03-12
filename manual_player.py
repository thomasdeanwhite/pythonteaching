from player import Player

class ManualPlayer(Player):

    def __init__(self, player_num):
        self.player_num = player_num
        self.name = input("Please enter your name:")

    def make_move(self, connect_four):
        print("|", end="")
        for i in range(connect_four.grid_size[1]):
            print("{}  ".format(i), end="")
        print("|")
        connect_four.print()
        move = self.input_int("Please enter a column:")

        while not connect_four.is_valid_move(move):
            print("Move invalid! ")
            move = self.input_int("Please enter a column:")
        return move

    def input_int(self, msg):
        x = input(msg)

        while not x.isdigit():
            print("Not a number...")
            x = input(msg)
        return int(x)

    def get_name(self):
        return self.name