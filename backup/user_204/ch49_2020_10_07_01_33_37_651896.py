def inverte_lista(lista):
    i = 0
    while i <= len(lista):
        lista.append(lista[i])
        del(lista[i])
        return lista
        i += 1
print(inverte_lista([1,2,3,4]))