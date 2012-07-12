from collections import defaultdict

LINES = [ (1,2,3),
          (4,5,6),
          (7,8,9),
          (1,4,7),
          (2,5,8),
          (3,6,9),
          (1,5,9),
          (3,5,7) ]

class Board(object):
    def __init__(self):
        self.pos_map = defaultdict(set)
        self.tok_map = {}

    def move(self, turn, pos1, pos2):
        self.pos_map[pos1].add(turn)
        self.pos_map[pos2].add(turn)
        self.tok_map[turn] = (pos1, pos2)

    def check_winner(self):
        for line in LINES:
            values = [self.pos_map[pos] for pos in line]
            if all(isinstance(v, str) for v in values):
                if all(v == 'X' for v in values):
                    return 'X'
                if all(v == 'O' for v in values):
                    return 'O'


class Game(object):
    def __init__(self):
        self.board = Board()
#    def move_random():
#        moves = []
#        for elem in self.board.pos_map:
#            moves+=list(elem)
#        next_move = max(moves)
#        placed = False
#        while not placed:
#next_move = max([ for elem in self.board.pos_map])

    def play(self):
        for turn in range(1, 10):
            pos1, pos2 = self.get_move(turn)
            self.board.move(turn, pos1, pos2)
            self.display()
            if board.has_cycle():
                choices = board.get_cycle_breaker()
                choice = self.get_user_choice(choices)
                board.collapse(choice)
                self.board.display()
            winner = board.check_winner()
            if winner:
                print winner, "wins!"
                return winner
        print "it's a draw!"

if __name__ == '__main__':
    b = Board()
    b.pos_map[1] = 'X'
    b.pos_map[2] = 'O'
    b.pos_map[3] = 'O'
    b.pos_map[4] = 'X'
    b.pos_map[5] = 'O'
    b.pos_map[6] = 'O'
    b.pos_map[7] = 'O'
    b.pos_map[8] = 'O'
    b.pos_map[9] = 'O'
    print b.check_winner()
