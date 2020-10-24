def traduz(lista,dicionario):
    lista2=[]
    for i in lista:
        if i in dicionario:
            lista2.append(dicionario[i])
            
    return lista2
            