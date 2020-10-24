def zera_negativos(lista):
    num_lista = len(lista)
    i=0
    
    while i < num_lista:
        if lista[i] < 0:
            lista [i] = 0
    i+=1