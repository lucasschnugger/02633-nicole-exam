import numpy as np
def gearing(ratio, cogwheels):
    BestRatio=999999
    for i in range(len(cogwheels)):
        for j in range(len(cogwheels)):
            if i!=j:
                RatioTest=cogwheels[i]/cogwheels[j]
                diff=abs(RatioTest-ratio)
                if diff < BestRatio:
                    BestRatio=diff
                    r=RatioTest
    return r


print(gearing(1.75, np.array([40,43,60,80])))

print(gearing(0.1, np.array([3,4,5,6,7,8,9,10])))
