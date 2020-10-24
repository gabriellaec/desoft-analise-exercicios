def inverte_dicionario(dicionario):
    saida = {}
    for nome, idade in dicionario.items():
        if idade not in saida:
            saida[idade] = []
        saida[idade].append(nome)
    return saida