def numero_no_indice(lista):
    lista2=[]
    for i in range(len(lista)-1):
        if lista[i]==i:
            lista2.append(lista[i])
            
    return lista2
