import numpy as np
def german_tank_problem(serialCodes):
    n=len(serialCodes)
    SerieNummer=np.zeros(n)
    for i in range(n):
        serialChar = serialCodes[i][0]
        serialNo = int(serialCodes[i][1:4])

        if serialChar == "A":
            SerieNummer[i] = 0 + serialNo + 1
        elif serialChar == "B":
            SerieNummer[i] = 1000 + serialNo + 1
        elif serialChar == "C":
            SerieNummer[i] = 2000 + serialNo + 1
        elif serialChar == "D":
            SerieNummer[i] = 3000 + serialNo + 1

    m = max(SerieNummer)
    N=np.round(m+(m/n)-1)

    return N
print(german_tank_problem(np.array(['C007','A911','B201','A038','A629'])))
