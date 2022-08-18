def romanToValue(roman):

    # værdi-tabel
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    maxSymbolValue = 0  # hold styr på max symbol-værdi, initialiseret til 0
    value = 0  # hold styr på total værdien, initialiseret til 0

    # Gennemløb symbolerne fra højre
    for n in reversed(range(len(roman))):
        # n er nu len(roman) --> 0, dvs. der tælles mod nul og der kan derfor itereres over symbolerne omvendt
        symbol = roman[n]  # symbolet vi er nået til, startende fra højre

        # Omdan symbol til tal-værdi
        symbolValue = table[symbol]

        # Hvis symbol-værdien er større eller lig med maksimum
        if symbolValue>=maxSymbolValue:
            maxSymbolValue=symbolValue
            value=value+symbolValue
            # Tilføj symbol-værdien til total-værdien
            # Opdater maksimum-værdien med symbol-værdien
        if symbolValue<maxSymbolValue:
            value=value-symbolValue
        # Hvis symbol-værdien er mindre end maksimum
            # Træk symbol-værdien fra total-værdien

    return value


print(romanToValue("XCIV"))
