def which_tetrahedral(t):
    n = 0
    T = 0
    while T < t:
        n += 1
        T = (n * (n + 1) * (n + 2)) / 6
    if T != t:
        n = 0
    return n
