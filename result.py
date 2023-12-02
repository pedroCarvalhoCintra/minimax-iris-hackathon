def result(s, a):
    s_mod = s.deepcopy()
    s_mod[a[0]][a[1]] = a[2]
    return s_mod
