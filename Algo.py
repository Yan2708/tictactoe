from math import inf


def evaluate(state):
    """
    Evalue la valeur statique de la partie
    :param state: etat de la partie
    :return: int (1 croix gagne, -1 rond, 0 nulle)
    """
    w = state.winner()
    if w == 'Draw' or w is None:
        return 0
    return 1 if w == False else -1


def alpha_beta_search(state, depth, alpha, beta, maximizingPlayer):
    """
    recherche du min max de la partie donnee
    :param state: etat de la partie
    :param depth: profondeur restante a explorer
    :param alpha
    :param beta
    :param maximizingPlayer: si c'est le tour du joueur a maximiser
    :return: le score max possible du joueur
    """
    moves = state.moves()
    # si la partie est finie ou que l'exploration en profondeur est atteint
    if depth == 0 or len(moves) == 0 or state.winner() is not None:
        return evaluate(state)
    if maximizingPlayer:
        max_eval = - inf
        for pos in moves:
            state.play(pos)
            val = alpha_beta_search(state, depth - 1, alpha, beta, False)
            state.play(pos, True)
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
            # elagage
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = inf
        for pos in moves:
            state.play(pos)
            val = alpha_beta_search(state, depth - 1, alpha, beta, True)
            state.play(pos, True)
            min_eval = min(min_eval, val)
            beta = min(beta, val)
            # elagage
            if beta <= alpha:
                break
        return min_eval


def get_best_move(state):
    """
    Donne le meilleur coup possible a partir d'un etat de partie
    :param state: etat de la partie
    :return: position du meilleur coup
    """
    best_score = -inf
    best_move = None
    for pos in state.moves():
        state.play(pos)
        score = alpha_beta_search(state, 9, -inf, inf, False)
        state.play(pos, True)
        if score > best_score:
            best_score = score
            best_move = pos
    return best_move
