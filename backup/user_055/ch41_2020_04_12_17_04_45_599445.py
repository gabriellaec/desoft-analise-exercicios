def zera_negativos(lista_valores):
    for i in lista_valores:
        if lista_valores[i] < 0:
            lista_valores[i] = 0
    return lista_valores