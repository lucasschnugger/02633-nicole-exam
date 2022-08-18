def loadBalance(runtime):
    minDiff=None
    k=0
    for n in range(len(runtime)-1):
        w1=runtime[:n+1]
        w2=runtime[n+1:]
        diff=abs(sum(w1)-sum(w2))
        if minDiff is None or diff < minDiff:
            minDiff = diff
            k = len(w1)
    return k

print(loadBalance([5, 2.5, 17, 1.5, 22, 3.5]))
