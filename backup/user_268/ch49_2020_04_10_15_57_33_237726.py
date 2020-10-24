def inverte_lista(lista):
    a = len(lista)
    for i in range(a):
        b = lista[i] 
        c = lista[-1 - (i)]
        lista[i] = c
        lista[-1 - (i)] = b
        
    return lista