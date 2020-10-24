def remove_vogais(palavra):
    i=0
    l=["a", "e", "i", "o", "u"]
    while i<len(palavra):
        if palavra[i] in l:
            palavra-=palavra[i]
        i+=1