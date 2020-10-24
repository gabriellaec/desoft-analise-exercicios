def verifica_preco(string, dic1, dic2):
    for k in dic1.keys():
        if k==string:
            cor=dic1[k]
    for i in dic2.keys():
        if i==cor:
            preco=dic2[i]
    return preco