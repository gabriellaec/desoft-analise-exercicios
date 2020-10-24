def remove_vogais(word):
    n=len(word)
    i=0
    m=""
    while i<n:
        if word[i] != "a":
            if word[i] != "e":
                if word[i] != "i":
                    if word[i] != "o":
                        if word[i] != "u":
                            m=m+word[i]
        i=i+1
    return m