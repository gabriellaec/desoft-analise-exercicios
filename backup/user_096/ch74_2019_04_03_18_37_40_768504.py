def conta_bigramas(string):
    lista = []
    saida = {}
    i=0
    while i<len(string)-1:
        lista.append(string[i]+string[i+1])
        i+=1
    for e in lista:
        if e not in saida:
            saida[e] = 1
        elif e in saida:
            saida[e] += 1
    return saida