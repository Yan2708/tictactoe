

from Algo import alpha_beta_search, get_best_move
from game import Game

g = Game()

while g.winner() is None:
    print(g)
    print('coups possibles ' + ' '.join([str(i) for i in g.moves()]))
    pos = None
    if g.current:
        while pos not in g.moves():
            try:
                pos = int(input('endroit ou jouer '))
            except Exception:
                print('coup impossible')
    else:
        pos = get_best_move(g)

    g.play(pos)
print(g)
w = g.winner()
print(w if 'Draw' == w else 'O wins' if False == w else 'X wins')
