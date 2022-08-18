def stem(text, suffixes):
    t=''  # t starter som en tom streng
    ListText=text.split(' ')  # opdeler text pr. mellemrum, så der haves hvert ord for sig i en liste
    ListSuffixes=suffixes.split(' ')  # opdeler suffixes pr. mellemrum, så der haves hver endelse for sig i en liste
    for i in ListText:  # for hvert ord i listen af ord; ordet haves i variablen 'i'
        word_has_no_suffix = True  # vi antager at ordet ikke har et suffix fra listen af endelser
        for j in ListSuffixes:  # for hver endelse i listen af endelser; endelsen haves i variablen 'j'
            if i.endswith(j) and word_has_no_suffix == True:  # hvis ordet 'i' slutter med endelsen 'j'
                word_has_no_suffix = False  # vi ved nu at ordet har en af endelserne
                if t=='':  # hvis 't' er en tom streng; dvs. vi er ved første ord
                    t=t+i.removesuffix(j)  # indsæt ordet 'i' uden endelsen 'j' i 't'
                else:  # ellers (hvis ikke 't' er en tom streng); dvs. vi ved at vi er ved ord 2 eller senere
                    t=t+' '+i.removesuffix(j)  # indsæt ordet 'i' uden endelsen 'j' i 't', men med en mellemrum foran
        if word_has_no_suffix == True:  # hvis ordet 'i' ikke havde nogle af endelserne; antagelsen holdt stik
            if t=='':
                t=t+i  # indsæt ordet 'i' i 't' (ingen endelse af fjerne)
            else:
                t=t+' '+i  # indsæt ordet 'i' i 't' (ingen endelse af fjerne), men med et mellemrum foran
    return t

print(stem('it is lovely days driving on the roads in the heatness','ness ly s ing'))
