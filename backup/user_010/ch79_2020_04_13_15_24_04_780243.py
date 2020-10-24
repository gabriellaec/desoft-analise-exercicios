def monta_dicionario (x,y):
    dic={}
    for i,chaves in enumerate(x):
        dic[chaves]=y[i]
    return dic