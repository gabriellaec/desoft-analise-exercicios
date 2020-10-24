def numero_no_indice(lista):
    lista2=[]
    for i in lista:
        if lista[i]==i:
            lista2.append(lista[i])
            
    return lista2
