def inverte_dicionario(dic):
    saida = {}
    for nome,idade in dic.items():
        if idade not in saida:
            saida[idade] = [nome]
        else:
            saida[idade] += [nome]
    return saida
        