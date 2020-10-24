def estritamente_crescente(lista)
    for item in lista:
        if lista[item]> lista[item+1]:
            lista.pop(item+1)
    return lista
