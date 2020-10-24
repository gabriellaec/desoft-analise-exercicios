def inverte_dicionario(dic):
    invertido = dict()
    for nome in dic:
        idade = dic[nome]
        if idade in invertido:
            invertido[idade].append(nome)
        else:
            invertido[idade] = [nome]
    return invertido