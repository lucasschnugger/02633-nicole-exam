# 'for'-loops bruges til at køre noget kode et bestemt antal gange
# Et 'for'-loop er bygget op således:
#   - 'for' keywordet
#   - angivelse af hvor mange gange loopet skal køre
#   - : (kolon) markerer hvornår koden indeni 'for'-loopet starter
# Skal en værdi bruges efterfølgende udenfor 'for'-loopet, skal den også være blevet defineret inden begyndelsen af 'for'-loopet


# Eksempel: 'for'-loop der kører 'x' antal gange
x = 10  # indsæt antal gange loopet skal køre
for n in range(x):
    print(n)
# 'for' slutter, når indenteringen er tilbage til samme niveau som 'for' keywordet.
# Der startes altid fra 0 i programmering --> bemærk dog at loopet printer 'x' tal, dvs. koden i loopet kører 'x' antal gange

print('')  # print blanke linjer for at adskille resultater

# Eksempel: 'for'-loop der kører så mange gange som der er ting i en liste
liste = ['æble', 'pære', 'kirsebær', 'vindrue', 'appelsin', 'klementin', 'mango', 'papaya', 'passionsfrugt', 'jordbær', 'fersken']
for frugt in liste:
    print(frugt)
# 'for' slutter, når indenteringen er tilbage til samme niveau som 'for' keywordet.
# Læg mærke til at for hver gang loopet kører, bliver den næste frugt fra listen sat ind i 'frugt' variablen. Dvs. der "itereres over listen af frugter".

print('')  # print blanke linjer for at adskille resultater

# Eksempel: 'for'-loop der lægger 'a' til 'x' 'n' antal gange
x = 10  # startværdi
a = 3  # tal der lægges til
n = 35  # antallet af gange loopet skal køre
for k in range(n):
    x = x + a
print(f'Værdien af x er nu: {x}')  # printer værdien af 'x' efter loopets afslutning
