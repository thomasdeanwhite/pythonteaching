from player import Player

class BekahPlayer(Player):

    def __init__(self, player_num):
        self.player_num = player_num
        
    def check_moves(self, move, connect_four):
        if connect_four.is_valid_move(move):
            connect_four.make_move(move)
            valid = 1
            connect = connect_four.max_in_row(self.player_num + 1)
        else:
            valid = 0
            connect = 0
        return(valid, connect)
    
    def check_all_moves(self, connect_four):
        best_connect = 0
        best_move = 0
        for i in range(connect_four.grid_size[1]):
            board = connect_four.copy()
            checked = self.check_moves(i, board)
            if checked[0] == 1:
                if checked[1] > best_connect:
                    best_connect = checked[1]
                    best_move = i
        return(best_move)

    def make_move(self, connect_four):
        # Returns a single integer representing the column
        # to drop a counter in
        move = self.check_all_moves(connect_four)
        return move

    def get_name(self):
        return "Bekah"
