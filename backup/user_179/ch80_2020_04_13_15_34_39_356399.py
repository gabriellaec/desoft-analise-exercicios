def interseccao_chaves (d1,d2):
    d1_chaves = list(d1.keys())
    d2_chaves = list(d2.keys())
    lista = []
    i = 0
    while i < len(d1_chaves):
        if d1_chaves[i] in d2_chaves:
            lista.append(d1_chaves[i])
            i = i + 1
        else:
            i = i + 1
    return lista