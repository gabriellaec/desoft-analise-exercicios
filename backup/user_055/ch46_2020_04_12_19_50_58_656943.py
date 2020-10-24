def numero_no_indice(lista_numeros):
    lista_numeros_indice = []
    x = 0
    for i in lista_numeros:
        if i == x:
            lista_numeros_indice.append(i)
        x += 1
    return lista_numeros_indice