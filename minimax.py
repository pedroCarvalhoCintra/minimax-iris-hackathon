import math

def actions(s, player) -> "list[tuple]":
    """
    s = game state;
    player = bool (False if Mini, True if Max)

    returns moves
    """
    moves = []
    mark = "x" if player else "o"

    for i in range(3):
        for j in range(3):
            if s[i][j] == " ":
                moves.append((i, j, mark))
    return moves


def result(s, a) -> list[list]:
    s_mod = s.deepcopy()
    s_mod[a[0]][a[1]] = a[2]
    return s_mod

def value(p) -> int:
    return 1 if p == "x" else -1


def terminal(s) -> "tuple[bool, int | None]":
    filled = 0
    # verifica se um dos jogadores ganhou o jogo
    for p in ["x", "o"]:
        # verifica se completou uma linha
        for lin in s:
            if (n := lin.count(p)) == 3:
                return (True, value(p))
            filled += n
        # verifica se completou uma coluna
        for i in range(3):
            if s[0][i] == p and s[1][i] == p and s[2][i] == p:
                return (True, value(p))
        # verifica se completou uma diagonal
        if s[1][1] == p and (
            (s[0][0] == p and s[2][2] == p) or (s[0][2] == p and s[2][0] == p)
        ):
            return (True, value(p))

    # verifica se o tabuleiro já foi inteiramente preenchido
    if filled == 9:
        return (True, 0)

    return (False, None)


def minimax(tab, max):
    t = terminal(tab)
    if t[0]:
        return t[1]
    elif max:
        v = -math.inf
        for a in actions(tab, max):
            v = max(v, minimax(result(tab, a), False))
        return v
    else:
        v = math.inf
        for a in actions(tab, max):
            v = min(v, minimax(result(tab, a), True))
            
        return v
    