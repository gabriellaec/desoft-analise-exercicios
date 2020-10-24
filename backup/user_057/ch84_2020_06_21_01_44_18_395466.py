def inverte_dicionario(dic):
    dic2 = {}
    for nome in dic.keys():
        idade = dic[nome]
        dic2[idade] = nome
        
    return dic2            