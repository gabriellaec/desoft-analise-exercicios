def inverte_dicionario(dict):
    novo_d = {}
    for nome, idade in dict.items():
        if idade not in novo_d:
            novo_d[idade] = [nome]
        else:
            novo_d[idade].append(nome)
    return novo_d