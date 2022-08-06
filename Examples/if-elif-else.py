# 'if', 'elif' og 'else' er keywords som kan bruges til at styre et programs flow
# De bruges til at tjekke om betingelser er sande og kun hvis det er tilfældet, bliver den efterfølgende kode kørt

# Overblik:
#   - 'if' (hvis) tjekker om en betingelse er sand, og kører så den efterfølgende kode.
#   - 'elif' (ellers hvis) ligesom 'if' men kun hvis den forudgående 'if' ikke var sand. Kan kun stå efter en 'if'.
#   - 'else' (ellers) kører den efterfølgende kode kun hvis de forudgående 'if' og/eller 'elif' ikke var sande. Kan kun stå efter en 'if' eller 'elif', men står altid sidst.
# Der SKAL ALTID startes med en 'if'.
# Dernæst kan der indsættes et vilkårligt antal 'elif'.
# Der kan vælges at afslutte med en 'else', men det er ikke et krav. 'else' kan ikke stå imellem en 'if' og en 'elif'.


# Eksempel: givet en årlig indkomst 'income' i DKK, fortælles om der betales topskat eller ej
income = 550001  # indtast årlig indkomst her --> test ved at indsætte forskellige værdier
topSkatGrænse = 550000
if income >= topSkatGrænse:
    print("Du skal betale topskat.")
# 'if' slutter, når indenteringen er tilbage til samme niveau som 'if' keywordet.
else:
    print("Du skal ikke betale topskat.")
# 'else' slutter, når indenteringen er tilbage til samme niveau som 'else' keywordet.

print('')  # print blanke linjer for at adskille resultater

# Eksempel: givet en årlig indkomst 'income' i DKK, fortælles hvilket sociale lag du tilhører
income = 380000  # indtast årlig indkomst her --> test ved at indsætte forskellige værdier
lagUnderklasse = 260000  # bruges egentlig ikke --> se koden nedenfor
lagMiddelklasse = 410000
lagHøjereMiddelklasse = 540000
lagOverklasse = 1040000
if income >= lagOverklasse:
    print("Du tilhører overklassen.")
elif income < lagOverklasse and income >= lagHøjereMiddelklasse:
    print("Du tilhører den højere middelklasse.")
elif income < lagHøjereMiddelklasse and income >= lagMiddelklasse:
    print("Du tilhører middelklassen.")
else:
    print("Du tilhører underklassen.")
