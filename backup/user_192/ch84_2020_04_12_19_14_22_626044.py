def inverte_dicionario(normal):
    invertido = dict()
    nome = list()
    for k, v in normal.items():
        if not v in invertido:
            invertido[v] = nome[k]
        else:
            invertido[v] = nome.append(k)
    return invertido