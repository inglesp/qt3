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
        print self.pos_map
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

    def display(self):
        self.pretty(self.lines(self.flat()))

    def flat(self):
        base = [[], [], [],
                [], [], [],
                [], [], []]
        for pos, turn in self.pos_map.items():
            base[pos-1].extend(list(turn))
        return base

    def lines(self, flatted):
        lined = []
        lined.append(flatted[:3])
        lined.append(flatted[3:6])
        lined.append(flatted[6:9])
        return lined

    def pretty(self, lines):
        for line in lines:
            print " " * (15 * 3 + 10)
            for i, col in enumerate(line):
                print ",".join(self.named(p) for p in col).center(30),
                if i < 2:
                    print "|",
            print
            print
            print "-" * (30 * 3 + 10)

    def named(self, n):
#        return ("O" if n % 2 == 0 else "X") + str(n)
        return n

def test_display():
    b = Board()
    b.move(1, 2, 3)
    b.move(2, 4, 5)
    b.move(3, 8, 9)
    flatted = b.flat()
    lines = b.lines(flatted)

    b.display()

    print "passing unit kind of tests"

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
    print b.check_winner()
    b.move(1, 2, 3)
    print b.__dict__
    test_display()
