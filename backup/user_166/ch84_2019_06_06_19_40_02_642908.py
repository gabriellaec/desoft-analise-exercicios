def inverte_dicionario(dict):
    dic = {}
    for nome,idade in dict.items():
        if idade not in dic:
            dic[idade]=[nome]
        else:
            dic[idade].append(nome)
    return dic