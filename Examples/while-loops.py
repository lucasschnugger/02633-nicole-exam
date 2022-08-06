# 'while'-loops bruges til at køre noget kode så længe en betingelse er sand
# Et 'while'-loop er bygget op således:
#   - 'while' keywordet
#   - betingelse for hvor længe loopet skal køre
#   - : (kolon) markerer hvornår koden indeni 'while'-loopet starter
# Skal en værdi bruges efterfølgende udenfor 'while'-loopet, skal den også være blevet defineret inden begyndelsen af 'while'-loopet


# Eksempel: 'while'-loop der kører indtil 'x' er større end eller lig med 'max'
max = 100  # værdien som 'x' skal nå, før loopet skal stoppe med at køre
x = 0  # startværdien af 'x'
count = 0  # antallet af kørsler i 'while'-loopet tælles op i denne variabel
while x < max:
    x = x + 3
    count = count + 1
    print(f'while-loop-iteration {count}, værdien af x er nu: {x}')
print(f'while-loopet kørte {count} antal gange og x nåede værdien {x}')

print('')  # print blanke linjer for at adskille resultater

# Eksempel: 'while'-loop med bruge af kontrol-variabler
max = 13125123
isBelowMax = True
x = 0
count = 0
while isBelowMax:
    x = x * 5 + 1
    count = count + 1
    print(f'while-loop-iteration {count}, værdien af x er nu: {x}')
    if x > max:
        isBelowMax = False  # loopet stopper først efter isBelowMax er sat til False
        print('x er nu større end max!')
print(f'while-loopet kørte {count} antal gange og x nåede værdien {x}')

print('')  # print blanke linjer for at adskille resultater

# Eksempel: uendeligt 'while'-loop, fordi betingelsen aldrig bliver falsk
x = 0
import time
while x % 2 == 0:  # x vil altid være lige, da der kun lægges 2 til
    x = x + 2
    print(x)
    time.sleep(2)  # venter 2 sek.
# Stop kørsel manuelt --> dette while-loop kører forevigt
