def inverte_dicionario(dic):
    novo = {}
    for nome, idade in dic.items():
        if idade not in novo.keys():
            novo[idade] = [nome]
        else:
            novo[idade].append(nome)
    return novo