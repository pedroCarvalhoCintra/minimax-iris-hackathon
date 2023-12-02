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
