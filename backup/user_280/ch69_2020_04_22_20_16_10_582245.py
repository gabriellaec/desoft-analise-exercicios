def junta_listas(lista1):
    lista2 = []
    i=0
    while i < len(lista1):
        j=0
        while j < len(lista1[i]):
            lista2.append(lista1[i][j])
            j+=1
        i+=1
    return lista2
            
        