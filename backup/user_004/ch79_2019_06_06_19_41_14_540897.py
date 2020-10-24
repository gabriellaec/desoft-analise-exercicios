def monta_dicionario(lista, lista1):
    dic = {}
    i = 0
    while i < len(lista):
        dic[lista[i]] = lista1[i]
        i+=1
    return dic
