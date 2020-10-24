def numero_no_indice(lista_numeros):
    lista_indice = []
    i = 0
    for numero in lista_numeros:
        if numero == i:
            lista_indice.append(numero)
        i += 1
    return lista_indice