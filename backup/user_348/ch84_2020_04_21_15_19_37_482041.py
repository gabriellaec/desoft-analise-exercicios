def inverte_dicionario (entrada):
    saida = {}
    for nome, idade in entrada.items():
        saida[idade] = nome
    return saida