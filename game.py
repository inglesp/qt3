from collections import defaultdict

class Board(object):
    def __init__(self):
        self.pos_map = defaultdict(set)
        self.tok_map = {}

    def move(self, turn, pos1, pos2):
        self.pos_map[pos1].add(turn)
        self.pos_map[pos2].add(turn)
        self.tok_map[turn] = (pos1, pos2)

    def display(self):
        print self.pretty(self.lines(self.flat()))

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
        return ("O" if n % 2 == 0 else "X") + str(n)

def test_display():
    b = Board()
    b.move(1, 2, 3)
    b.move(2, 4, 5)
    b.move(3, 8, 9)
    flatted = b.flat()
    assert flatted == [[], [1], [1],
                       [2], [2], [],
                       [], [3], [3]], flatted

    lines = b.lines(flatted)
    assert lines == [[[], [1], [1]],
                     [[2], [2], []],
                     [[], [3], [3]]], lines

    assert b.named(1) == "X1"
    assert b.named(2) == "O2"
    assert b.named(3) == "X3"

    b.display()

    print "passing unit kind of tests"

class Game(object):
    def __init__(self):
        self.board = Board()

    def play(self):
        for turn in range(1, 10):
            pos1, pos2 = self.get_move(i)
            self.board.move(turn, pos1, pos2)
            self.display()
            if board.has_cycle():
                choices = board.get_cycle_breaker()
                choice = self.get_user_choice(choices)
                board.collapse(choice)
                self.board.display()
            board.check_winner()


if __name__ == '__main__':
    b = Board()
    b.move(1, 2, 3)
    print b.__dict__
    test_display()
