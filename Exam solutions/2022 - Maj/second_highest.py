import numpy as np
def second_highest(A):
    UniqueValues=np.unique(A)  # finder unikke værdier i A --> kun én forekomst af hvert tal
    if len(UniqueValues) < 2:  # hvis der er mindre end 2 forskellige tal i A
        return 0
    y = 0
    Highest=np.max(A)
    RemoveHighest=A[A!=Highest]
    SecondHighest=np.max(RemoveHighest)
    for num in RemoveHighest:
        if SecondHighest==num:
            y=y+1
    return y




A = np.array([
    [10,10,5],
    [2,10,7],
    [10,10,10]
])
print(second_highest(A))

def second_highest(A):
    unique_values = np.unique(matrix)
    if len(unique_values) < 2:
        return 0
    second_high_val = unique_values[-2]
    y = len(np.where(A == second_high_val)[0]) #== sammenligner venstre med højre side
    return y
