def numero_no_indice(lista):
    i=0
    lista_2=[]
    while i<len(lista):
        if lista[i]==i:
            lista_2.append(lista[i])
        i+=1
    return lista_2
        
        