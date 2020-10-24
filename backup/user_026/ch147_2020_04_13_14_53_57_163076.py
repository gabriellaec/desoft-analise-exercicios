def mais_frequente(lista):
    dic = {}
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    lista= lista(dic.keys())
    lista2 = lista(dic.values())
    
    return lista[lista2.index(max(lista2))]