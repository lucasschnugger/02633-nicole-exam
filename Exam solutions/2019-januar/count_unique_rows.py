import numpy as np
def count_unique_rows(x):
    sorted = np.sort(x)  # sorterer hver række i x
    unique_rows_sorted = np.unique(sorted, axis=0)  # finder unikke rækker i sorted
    number_of_unique_rows = len(unique_rows_sorted)  # tæller antal unikke rækker
    unique_rows_x = np.unique(x, axis=0)  # finder unikke rækker i x (for at fjerne flere af samme rækker der starter med 2)
    rows_starting_with_2 = 0  # tælle-variabel til rækker startende med 2
    for row in unique_rows_x:  # for hver række i x's unikke rækker (ikke sorteret)
        if row[0] == 2:  # hvis første tal i rækken er lig med 2
            rows_starting_with_2 = rows_starting_with_2 + 1  # tæl 1 op i tællevariablen
    count = number_of_unique_rows - rows_starting_with_2  # antal unikke rækker findes ved at trække antal rækker startende med 2 fra antallet af unikke rækker
    return count


x = np.array([
    [1,2,3],
    [1,2,3],
    [2,2,3],
    [3,1,2],
    [1,2,4],
    [1,4,2]
])
print(count_unique_rows(x))