def inverte_dicionario(dicionario):
    dic = {}
    for nome in dicionario:
        idade = dicionario[nome]
        if not idade in dic:
            dic[idade] = lista
            lista.append(nome)
        else:
            lista.append(nome)
    return dic