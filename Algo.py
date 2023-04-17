from math import inf


def evaluate(state):
    if state.winner() == 'Draw':
        return 0
    if state.winner() is None:
        return score_count(state, True) - score_count(state, False)
    return 1 if state.winner() is True else -1


def score_count(state, player):
    score = 0
    # tableau contenant toutes les lignes gagnantes
    tabs = []
    for i in range(3):
        tabs.append(state.board[(i * 3):(i * 3) + 3])
        tabs.append(state.board[i::3])
    tabs.append(state.board[::4])
    tabs.append(state.board[2:7:2])
    # lorsqu'il y a 1 ou 2 pieces sur les lignes colonnes ou diagonales
    for line in tabs:
        score += 40 if line.count(not player) == 2 and line.count(player) == 1 else 0
        score += 10 if line.count(player) == 2 and line.count(None) == 1 else 0
        score += 1 if line.count(player) == 1 and line.count(None) == 2 else 0
    return score


def alpha_beta_search(state, depth, alpha, beta, maximizingPlayer):
    # return max_value(state, depth, -inf, inf, player)

    if depth == 0 or state.winner() is not None:
        return evaluate(state)
    moves = state.moves()
    if maximizingPlayer:
        max_eval = - inf
        for pos in moves:

            val = alpha_beta_search(state.child_state(pos,state.current), depth - 1, alpha, beta, False)
            # print(c_state, val, pos)
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = inf
        for pos in moves:
            val = alpha_beta_search(state.child_state(pos,state.current), depth - 1, alpha, beta, True)
            min_eval = min(min_eval, val)
            alpha = min(alpha, val)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(state):
    best_score = -inf
    best_move = None
    for pos in state.moves():

        score = alpha_beta_search(state, 1, -inf, inf, True)
        print(pos,'\n',state.child_state(pos,False),score)
        if score > best_score:
            best_score = score
            best_move = pos
    return best_move
