def inverte_dicionario(dic):
    nomes=list(dic.keys())
    idade=list(dic.values())
    dic1=dict(zip(idade,nomes))
    return dic1
