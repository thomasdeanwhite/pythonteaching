
from random_player import RandomPlayer
from jackie_player import JackiePlayer

from badplayer import BekahPlayer

class ConnectFour():

    def __init__(self):
        # initialize board variables
        self.grid_size = (6, 7)
        self.board = []
        self.turn = 0
        # two random players
        self.players = [BekahPlayer(0), JackiePlayer(1)]

        self.playing = False
        self.output = True

    def start_game(self):
        # empty board and set turn to 0. Set playing var to True to allow moves to be made.
        for i in range(self.grid_size[0]):
            self.board.append([0 for _ in range(self.grid_size[1])])

        self.turn = 0
        self.playing = True

    def print(self):
        if not self.output:
            return
        # print top border
        for _ in range(len(self.board[0])+1):
            print("---", end='')
        print()
        for r in range(len(self.board)):
            # print board in reverse order (so row 0 is printed last)
            row = self.board[len(self.board)-r-1]
            print("|", end='')
            for cell in row:
                # print X or O depending on piece in cell.
                print(" " if cell == 0 else "X" if cell == 1 else "O", " ", end='')
            print("|")

        #print bottom border
        for _ in range(len(self.board[0])+1):
            print("-", "-", end='')
        print()

    def next_turn(self):
        if self.playing:
            move = self.players[self.turn].make_move(self)

            self.make_move(move)

    def make_move(self, move):
        if self.playing:
            # is move valid (is column full?)
            if self.is_valid_move(move):
                # get row to insert piece in
                i = 0
                while self.board[i][move] != 0:
                    i += 1

                # insert piece
                self.board[i][move] = self.turn + 1

                # is there a winner?
                if (self.has_won(self.turn+1)):
                    self.playing = False
                    if self.output:
                        print("Winner! Player", self.turn+1, "[X]" if self.turn == 0 else "[O]", self.players[self.turn].get_name())

                # is there at least one free column or is it a tie?
                game_in_progress = False
                for i in range(len(self.board)):
                    if self.is_valid_move(i):
                        game_in_progress = True

                # was no column free?
                if not game_in_progress:
                    self.playing = False
                    if self.output:
                        print("It's a draw!")

                #change players
                self.turn += 1
                self.turn = self.turn % 2

    def has_won(self, player):
        return self.max_in_row(player) >= 4

    def max_in_row(self, player):
        max = 0
        # start from every piece on board
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):

                # get number of pieces in a row in 8 directions
                for i in range(2):
                    for j in range(2):
                        # i == j == 0 could cause infinite looping on a single grid cell (adding 0 to x and y).
                        # Remove this possibility
                        if i == j and i == 1:
                            continue
                        in_row = self._has_won(player, x, y, i-1, j-1, 0)
                        if in_row > max:
                            max = in_row
        return max

    def _has_won(self, player, x, y, dx, dy, count):
        if x < 0 or x >= self.grid_size[0] or y < 0 or y >= self.grid_size[1]:
            return count
        if self.board[x][y] == player:
            return self._has_won(player, x+dx, y+dy, dx, dy, count+1)
        return count

    def is_valid_move(self, move):
        # see if move can be made in this column
        return self.board[-1][move] == 0

    def copy(self):
        # deep copy all variables to another memory address
        c = ConnectFour()
        c.grid_size = self.grid_size
        c.board = []
        c.playing = self.playing
        c.turn = self.turn
        c.disable_output()
        for row in self.board:
            l = []
            for cell in row:
                l.append(cell)
            c.board.append(l)
        return c

    def get_winner(self):
        if not self.playing:
            return 1 - self.turn
        return -1

    def disable_output(self):
        self.output = False




connect_four = ConnectFour()

connect_four.start_game()

while(connect_four.playing):
    connect_four.next_turn()
    connect_four.print()

win_list = []    
for i in range(1000):
    connect_four = ConnectFour()
    connect_four.disable_output()
    connect_four.start_game()
    while(connect_four.playing):
        connect_four.next_turn()
        connect_four.print()
    win_list.append(1-connect_four.turn)

print(win_list)

