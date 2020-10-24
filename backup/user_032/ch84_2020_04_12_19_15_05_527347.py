def inverte_dicionario(dicionario):
    dicionario_invertido = {}
    for key in dicionario:
        val = dicionario[key]
        if val not in dicionario_invertido:
            dicionario_invertido[val]=key
        else:
            dicionario_invertido[val].append(key)
    return dicionario_invertido