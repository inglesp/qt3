from collections import defaultdict

class Board(object):
    def __init__(self):
        self.pos_map = defaultdict(set)
        self.tok_map = {}

    def move(self, turn, pos1, pos2):
        self.pos_map[pos1].add(turn)
        self.pos_map[pos2].add(turn)
        self.tok_map[turn] = (pos1, pos2)

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
