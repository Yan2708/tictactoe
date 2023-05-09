class Game:

    def __init__(self, *args):
        self.board = [None for _ in range(9)] if len(args) == 0 else args[0]
        self.current = True
        self.turn = 0

    def __str__(self):
        sb = ''
        for i in range(9):
            sb += '_ ' if self.board[i] is None else 'X ' if self.board[i] is True else 'O '
            if (i + 1) % 3 == 0:
                sb += '\n'
        return sb

    def play(self, pos, unplay=False):
        """
        joue un coup
        :param pos: la position ou poser le pion
        :param unplay: si true remplie le pion a la pos specifie par None et revient au tour precedent
        """
        self.board[pos] = None if unplay else self.current
        self.current = not self.current
        self.turn += -1 if unplay else 1

    def moves(self):
        """
        Coups possibles
        :return: liste des coups possibles
        """
        return [i for i, v in enumerate(self.board) if v is None]

    def winner(self):
        """
        Verifie si la partie est finie
        :return: Draw si nulle, True si croix gagne, False si rond gagne, None si la partie n'est pas finie
        """
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
