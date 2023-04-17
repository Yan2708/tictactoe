class Game:

    def __init__(self, *args):
        self.board = [None for _ in range(9)] if len(args) == 0 else args[0]
        self.current = True
        self.turn = 0

    def __str__(self):
        sb = ''
        for i in range(9):
            sb += 'N ' if self.board[i] is None else 'X ' if self.board[i] is True else 'O '
            if (i + 1) % 3 == 0:
                sb += '\n'
        return sb

    def play(self, pos):
        self.board[pos] = self.current
        self.current = not self.current
        self.turn += 1

    def moves(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def child_state(self, pos,player):
        g=Game(self.board[:])
        g.current=player
        g.play(pos)
        return g

    def winner(self):
        # check lines and rows
        for i in range(3):
            if set(self.board[(i * 3):(i * 3) + 3]) == set([True]) or set(self.board[(i * 3):(i * 3) + 3]) == set(
                    [False]) \
                    or set(self.board[i::3]) == set([True]) or set(self.board[i::3]) == set([False]):
                return self.board[(i * 3) + i]
        # check diagonals
        if set(self.board[::4]) == set([True]) or set(self.board[::4]) == set([False]):
            return self.board[0]
        if set(self.board[2:7:2]) == set([True]) or set(self.board[2:7:2]) == set([False]):
            return self.board[2]
        # check draw
        if None not in self.board:
            return 'Draw'
        return None
