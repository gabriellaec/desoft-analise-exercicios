def inverte_dicionario(dicionario):
    dicionario_invertido = {}
    for c,v in dicionario.items():
        lista = []
        if v not in dicionario_invertido:
            lista.append(c)
            dicionario_invertido[v] = lista
        else:
            dicionario_invertido[v].append(c)

    return dicionario_invertido