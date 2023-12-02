def result(s, a) -> list[list]:
    s_mod = s.deepcopy()
    s_mod[a[0]][a[1]] = a[2]
    return s_mod
