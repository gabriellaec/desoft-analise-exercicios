def estritamente_crescente(lista):
    if len(lista) == 0: 
        return lista
    nova_lista = [lista[0]]
    for i in range(1,len(lista)):
        if lista[i] > lista[i-1]:
            nova_lista.append(lista[i])
    return nova_lista