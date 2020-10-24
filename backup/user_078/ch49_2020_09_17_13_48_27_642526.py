def inverte_lista(lista):
    imax = len(lista) - 1
    lista_invertida = []
    
    while imax >= 0:
        lista_invertida.append(lista[imax])
        imax -= 1
        
    return lista_invertida
