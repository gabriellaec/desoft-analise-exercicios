def mais_frequente(lista):
    dic = {x:lista.count(x) for x in lista}
    return max(dic,key=dic.get)