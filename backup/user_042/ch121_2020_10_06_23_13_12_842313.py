def subtracao_de_listas(lista1, lista2):
    i = 0
    n= 0
    lista_nova = []
    while n < len(lista2):
        if lista1[i] != lista2[n]:
            lista_nova.append(lista1[i])
        if lista1[i] != lista2[n]:
            lista_nova.append(lista1[i])
            n+=1
        if lista1 == []:
            lista_nova = []
        if lista2 == []:
            lista_nova = lista1
        i += 1
        n+= 1
    return lista_nova 
            
        
        
    