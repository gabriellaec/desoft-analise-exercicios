def inverte_dicionario(dicionario):
    novo = {}
    for k, v in dicionario.items():
        if v in novo:
            lista.append(k)
            novo[v] = lista
        else:
            lista = [k]
            novo[v] = lista   
    return novo