def inverte_dicionario(dicionario):
    dicionario2 = {}
    for i in dicionario:
        dicionario2[i]= dicionario[i[i]]
        dicionario2[i[i]] = dicionario[i]
    return dicionario

    