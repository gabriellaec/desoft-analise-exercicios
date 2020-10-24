lista = [1, 5, 3, 7, 8]
def estritamente_crescente(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if lista[i+1] > lista[i]:
            lista2.append(lista[i])
        i += 1
    return lista2