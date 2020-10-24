def inverte_dicionario (d1):
    d2 = {}
    for nome in d1:
        if d1[nome] not in d2:
            lista = []
            d2[d1[nome]] = lista.append(nome)
        if d1[nome] in d2:
            lista = d2[d1[nome]]
            lista.append(nome)
    return d2
    