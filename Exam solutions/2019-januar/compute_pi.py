import math


def compute_pi(c, t):

    if t == 2:  # hvis t er 2, skal bruges den ene formel
        terms = 0  # vi udregner værdien af termerne, derfor starter vi i 0
        for n in range(c):
            terms = terms + 1/((n+1)**2)  # se formel 1; udregning af term. Brug n+1, da n starter på 0
        value = math.sqrt(6*terms)  # se formel 1; kvadratrod af 6 * termerne

    elif t == 4:  # hvis t er 4, skal bruges den anden formel
        terms = 0  # vi udregner værdien af termerne, derfor starter vi i 0
        for n in range(c):
            terms = terms + 1/((n+1)**4)  # se formel 2; udregning af term. Brug n+1, da n starter på 0
        value = (90*terms)**(1/4)  # se formel 2; 4-rod (fjerderoden) af 90 * termerne

    return value

print(compute_pi(3, 2))
print(compute_pi(2, 4))