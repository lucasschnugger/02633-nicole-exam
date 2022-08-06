# En funktion defineres ved en function definition
# En function definition består af:
#   - def keywordet, som fortæller at det er en definition af en funktion
#   - navnet på funktionen
#   - de data som funktionen skal bruge for at køre, omsluttet af parantes
#   - : (kolon) markerer hvornår koden som funktionen kører starter
# En funktion kan returnere en værdi, men behøver det ikke


# Eksempel: funktion der tjekker og skriver om tallet 'n' er lige eller ulige
#   - Funktionsnavn: isEven
#   - Data: n (tal)
#   - Returnerer ikke nogen værdi
def isEven(n):
    # %-operatoren (kaldet modulo), giver restmængden ved gentagen division med det angivne tal, i dette tilfælde 2
    # Dvs. at hvis n=40, går det op i 2 og restmængden er 0 --> betyder at tallet n=40 er lige
    # Dvs. at hvis n=43, går 42 op i 2 og restmængden er 1 --> betyder at tallet n=43 er ulige
    if n % 2 == 0:
        print(True)
    else:
        print(False)
    return
# Funktionen slutter, når indenteringen er tilbage til samme niveau som definitionen af funktionen.


# Eksempel: funktion der tæller antallet af karakteren 'c' i sætningen 's'
#   - Funktionsnavn: countChar
#   - Data: s (sætning), c (karakter)
#   - Returnerer antallet 'count' af karakteren 'c' i sætningen 's'
def countChar(s, c):
    count = 0
    for character in s:
        if character == c:
            count = count +1
    return count
# Funktionen slutter, når indenteringen er tilbage til samme niveau som definitionen af funktionen.


# Test 'isEven':
print('isEven test 1:')
isEven(0)
print('isEven test 2:')
isEven(43)
print('isEven test 3:')
isEven(90)
print('isEven test 4:')
isEven(1123145191)
# Da 'isEven' ikke returnerer en værdi, bliver svaret skrevet på særskilt linje

print('\n')  # print blanke linjer for at adskille resultater

# Test 'countChar':
print(f'countChar test 1: {countChar("en lille gris gik på markedet", "l")}')
print(f'countChar test 2: {countChar("rødgrød med fløde gør børnene søde", "ø")}')
print(f'countChar test 3: {countChar("nicole er super-god til programmering", "k")}')
print(f'countChar test 4: {countChar("hejsa", "j")}')
# Da 'countChar' returnerer en talværdi, kan den bruges som ovenfor i print-funktionen til at indsætte svaret som funktionen giver
