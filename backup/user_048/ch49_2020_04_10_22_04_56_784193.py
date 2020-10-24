def inverte_lista(lista):     
    alcance=int(len(lista)/2)
    for i in range(alcance):
        lista[i], lista[len(lista)-1-i] = lista[len(lista)-1-i], lista[i]
    return lista