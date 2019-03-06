
class Player():

    def __init__(self, player_num):
        pass

    def make_move(self, connect_four):
        # Returns a single integer representing the column
        # to drop a counter in
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()