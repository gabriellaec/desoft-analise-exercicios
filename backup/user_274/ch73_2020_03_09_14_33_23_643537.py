def remove_vogais(word):
    n=len(word)
    i=0
    m=""
    while i<n:
        if word[i] != "a" or "e" or "i" or "o" or "u":
            m=m+word[i]
        i=i+1
    return m