def subtracao_de_listas(lista1, lista2):
    i = 0
    l1 = len(lista1)
    lista_nova = []
    while i < l1:
        if lista1[i] != lista2[i]:
            lista_nova.append(lista1[i])
        if lista1[i] != lista2[i+1]:
            lista_nova.append(lista1[i])
        i += 1
    return lista_nova 
            
        
        
    