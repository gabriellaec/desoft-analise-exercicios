def zera_negativos(lista):
    
    lista = list(lista)
    
    index = 0
    
    for i in lista:
        if i < 0: lista[index] = 0
        index += 1
    
    return lista