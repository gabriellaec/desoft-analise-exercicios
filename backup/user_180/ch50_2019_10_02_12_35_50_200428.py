def numero_no_indice(lista_numeros):
    lista_indice = []
    for numero in lista_numeros:
        if numero == lista_numeros[numero]:
            lista_indice.append(numero)
    return lista_indice