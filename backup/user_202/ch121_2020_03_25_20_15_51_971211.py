def subtracao_de_listas(lista1, lista2 ):
    m = len(lista1)
    i = 0
    a = 0
    lista3 = [0]*m
    while i < m: 
    	if lista1[i] != lista2[i]:
            lista3[a] = lista1[i] 
            a += 1
        i += 1
    return(lista3)
        
        