def inverte_dicionario(x):
    dic= {}
    for nome, idade in x.items():
        if idade not in dic:
            dic[idade] = [nome]
        else:
            dic[idade].append(nome)
    return dic