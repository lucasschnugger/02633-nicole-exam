def flowering_plants(G, m):
    n = 0
    for row in G:
        if row[0] == 0 and row[1] == 0:
            n += 1
        if row[0] == row[1] and m == row[0]:
            n += 1
        elif row[0] < row[1]:
            if row[0] <= m <= row[1]:
                n += 1
        elif row[0] > row[1]:
            if row[0] >= m >= row[1]:
                n += 1
    return n
