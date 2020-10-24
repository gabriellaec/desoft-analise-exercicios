def estritamente_crescente(n):
    lista = [n]
    for i in range(len(lista)):
        if lista[i] < lista[i-1]:
            del lista[i]
    return lista