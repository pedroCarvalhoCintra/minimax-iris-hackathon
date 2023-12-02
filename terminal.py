def terminal(s) -> bool:
    filled = 0
    # verifica se um dos jogadores ganhou o jogo
    for p in ["x", "o"]:
        # verifica se completou uma linha
        for lin in s:
            if (n := lin.count(p)) == 3:
                return True
            filled += n
        # verifica se completou uma coluna
        for i in range(3):
            if s[0][i] == p and s[1][i] == p and s[2][i] == p:
                return True
        # verifica se completou uma diagonal
        if s[1][1] == p and (
            (s[0][0] == p and s[2][2] == p) or (s[0][2] == p and s[2][0] == p)
        ):
            return True

    # verifica se o tabuleiro já foi inteiramente preenchido
    if filled == 9:
        return True

    return False
