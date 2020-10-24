def inverte_dicionario(dicionario):
    i = 0
    dicionario2 = {}
    for i in dicionario:
        dicionario2[i]= dicionario[i[i]]
        dicionario2[i[i]] = dicionario[i]
    return dicionario

    