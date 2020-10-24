def inverte_dicionario(dic):
    dic2 = {}
    for nome in dic.keys():
        idade = dic[nome]
        if nome not in dic2.vallues():
            dic2[idade] = [nome]
        else: 
            dic2[idade].append(nome)
    return dic2            