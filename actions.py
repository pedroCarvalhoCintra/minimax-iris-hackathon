def actions(s, player) -> "list[tuple]":
    """
    s = game state;

    returns moves
    """
    moves = []

    for i in range(3):
        for j in range(3):
            if s[i][j] == ' ':
                moves.append((i,j))
    return moves