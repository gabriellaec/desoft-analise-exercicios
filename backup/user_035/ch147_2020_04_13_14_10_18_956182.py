def mais_frequente(lista):
    dic = {}
    i = 0
    while i <= len(lista)-1:
        if lista[i] not in dic:
            dic[lista[i]] = 1
            i += 1
        else:
            dic[lista[i]] += 1
            i += 1
    lista1 = list(dic.keys())
    lista2 = list(dic.values())
    
    return lista1[lista2.index(max(lista2))]