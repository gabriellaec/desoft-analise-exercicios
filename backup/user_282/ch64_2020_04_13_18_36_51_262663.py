def acha_bigramas(palavra):
    count = list()
    letras = list(palavra)
    for e in range(len(letras)-1):
        bi = letras[e] + letras[e+1]
        if bi not in count:
            count.append(bi)
    return count