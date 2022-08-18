import numpy as np
def count_peaks(A):
    c = 0
    for n in range(len(A)):
        for v in range(len(A[0])):
            number = A[n][v]

            hasPeak = False
            if n > 0:
                up = A[n-1][v]
                hasPeak = hasPeak or (number > up and abs(number-up) >= 2)
            if n < len(A)-1:
                down = A[n+1][v]
                hasPeak = hasPeak or (number > down and abs(number - down) >= 2)
            if v > 0:
                left = A[n][v-1]
                hasPeak = hasPeak or (number > left and abs(number - left) >= 2)
            if v < len(A[0])-1:
                right = A[n][v+1]
                hasPeak = hasPeak or (number > right and abs(number - right) >= 2)

            if hasPeak:
                c = c + 1
    return c

A = np.array([
    [1,2,3,5,3,7,7.1],
    [3,3,3,4,4,7,7.3]
])
print(count_peaks(A))