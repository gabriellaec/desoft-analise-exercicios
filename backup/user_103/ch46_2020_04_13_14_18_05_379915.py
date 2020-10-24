def numero_no_indice(lista):
    lista1=[]
    i=0
    for i in range (len(lista)): 
        if lista[i]==i:
            lista1.append(lista[i])
    return lista1 