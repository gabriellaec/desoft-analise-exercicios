def numero_no_indice(lista):
    lista_indice = []
    for numero in lista:
        if numero == lista[numero]:
            lista_indice.append(numero)
    return lista_indice