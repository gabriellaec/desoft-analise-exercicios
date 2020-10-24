def mais_frequente(lista):
    dic={}
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1          
        
    lista1=dic.keys()
    lista2=dic.values()
    return lista1[lista2.index(max(lista2))]


        