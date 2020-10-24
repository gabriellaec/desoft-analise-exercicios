def inverte_dicionario (entrada):
    saida = {}
    for nome, idade in entrada.items():
        if idade not in saida:
            saida[idade] = []
        saida[idade].append(nome)
    return saida