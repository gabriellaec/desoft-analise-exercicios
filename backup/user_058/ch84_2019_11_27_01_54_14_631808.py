def inverte_dicionario(dicionario):
    invertido = {}
    for k,v in dicionario.items():
        if v not in invertido.keys():
            invertido[v] = [k]
        elif v in invertido.keys():
            invertido[v] += [k]
    return invertido