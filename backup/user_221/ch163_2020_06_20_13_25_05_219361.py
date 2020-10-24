def calcula_media(lista):
    i = 0
    s = 0
    d = 0
    while i < len(lista):
        for nome, nota in lista[i].items():
            s += lista[i][nome]
            d += 1
        i += 1
    y = s/d
    return y
    