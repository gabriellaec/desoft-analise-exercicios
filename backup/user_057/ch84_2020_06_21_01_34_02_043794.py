def inverte_dicionario(dic):
    dic2 = {}
    for nome in dic.keys():
        idade = dic[nome]
        if nome in dic2.vallues():
            dic2[idade].append(nome)
        else:
            dic2[idade] = [nome]
    return dic2            