
lista2 = []
def numero_no_indice(lista):
    for i in range(len(lista)):
        if i == lista[i]:
            lista2.append(i)
    return lista2