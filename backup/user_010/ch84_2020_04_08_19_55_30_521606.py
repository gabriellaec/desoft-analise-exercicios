def inverte_dicionario(dic):
    dic2={}
    for chave,valor in dic.items():
        if valor not in dic2:
            dic2[valor]=[]
            dic2[valor].append(chave)
        else:
            dic2[valor].append(chave)
    return dic2