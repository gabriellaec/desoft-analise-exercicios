def mais_frequente(lista):
    dicio = {}
    for a in lista:
        if a in dicio:
            dicio[a] += 1
        else:
            dicio[a]=1
    e = 0
    palavra = ''
    for p,o in dicio.items():
        if o > e:
            e = o
            palavra = p
    return palavra
    