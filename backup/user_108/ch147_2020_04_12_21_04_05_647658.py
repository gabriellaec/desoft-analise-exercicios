def mais_frequente(lista):
    dic = {x:lista.count(x) for x in lista}
    valor = max(dic.values())
    return list(dic.keys())[list(dic.values()).index(valor)]