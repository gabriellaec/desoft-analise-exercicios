
def numero_no_indice(lista):
    lista2 = []
    for i in range(len(lista)):
        if i == lista[i]:
            lista2.append(i)
    return lista2