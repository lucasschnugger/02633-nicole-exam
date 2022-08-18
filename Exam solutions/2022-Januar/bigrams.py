import numpy as np
def bigrams(s):

    bigrams_count = {}  # tomt opslagsværk til at gemme fundne bigrammer og antal der er fundet

    wordlist = s.split(' ')  # del ordlisten op til en liste af enkelte ord
    for word in wordlist:  # for hvert ord i ordlisten
        if len(word) >= 2:  # hvis ordet er mindst 2 bogstaver (ord på 1 bogstav har ikke bigrammer)
            for n in range(len(word)):  # loop over antal bogstaver i ordet; 0 til antal bogstaver i ordet
                if n < len(word)-1:  # hvis vi IKKE er på sidste bogstavs plads; ved sidste bogstav ved vi der ikke er flere bigrammer
                    bigram = word[n] + word[n+1]  # bigrammet er bogstavet på n's plads + det næste bogstav
                    if bigrams_count.get(bigram) == None:  # hvis bigrammet IKKE er tilføjet til opslagsværket
                        bigrams_count[bigram] = 1  # indsæt bigrammet i opslagsværket og sæt det til 1 forekomst
                    else:  # ellers; hvis bigrammet er tilføjet i opslagsværket allerede
                        bigrams_count[bigram] = bigrams_count[bigram] + 1  # tæl 1 op for bigrammet i opslagsværket

    values = np.array(list(bigrams_count.values()))  # omdan de optællede forekomster til et numpy array (kun værdierne)
    values.sort()  # sorter listen af bigram-forekomster (mindst til højest)
    values = np.flip(values)  # vend listen af bigram-forekomster om (højest til mindst)
    c = values[:5]  # tag de 5 første værdier af bigram-forekomster (sorteret ovenfor, således at de 5 største værdier står først)

    return c


print(bigrams('sing a song son so often or sign off'))