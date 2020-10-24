def estritamente_crescente(lista):
    lista_crescente = []
    for numero in lista:
        if numero >= lista[0]:
            lista_crescente.append(numero)
    return lista_crescente