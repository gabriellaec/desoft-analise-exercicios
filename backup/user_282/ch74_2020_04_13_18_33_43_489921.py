def conta_bigramas(palavra):
    count = dict()
    letras = list(palavra)
    for e in range(len(letras)-1):
        bi = letras[e] + letras[e+1]
        if bi in count:
            count[bi] += 1
        else:
            count[bi] = 1
    return count