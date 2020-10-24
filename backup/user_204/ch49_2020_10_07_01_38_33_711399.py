def inverte_lista(lista):
    i = 0
    inicio = len(lista)
    while i <= len(lista):
        lista.append(lista[i])
        i += 1
    del(lista[inicio])
    return lista
    

print(inverte_lista([1,2,3,4]))