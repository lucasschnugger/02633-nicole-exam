import numpy as np
def count_novel(text):
    novel_words = np.array([])  # tom numpy vector; til at indsætte unikke ord
    c = np.array([])  # tom numpy vector; til at indsætte forekomster af unikke ord indtil videre
    wordlist = text.split(' ')  # opdeler ordlisten i enkelte ord
    for word in wordlist:  # for hvert ord i ordlisten
        if novel_words.__contains__(word) == False:  # hvis vector ikke allerede har fået indsat ordet i word
            novel_words = np.append(novel_words, word)  # indsæt ordet word i vectoren for unikke ord
        c = np.append(c, len(novel_words))  # indsæt antallet af allerede sete unikke ord i resultat vectoren
    return c

print(count_novel('the man and another man walked down the street'))