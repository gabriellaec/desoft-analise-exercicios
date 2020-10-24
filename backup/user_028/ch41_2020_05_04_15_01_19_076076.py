def zera_negativos(lista):
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i] < 0:
            lista.append(0)
        else:
            lista.append(lista[i])
    return lista2  
   
            