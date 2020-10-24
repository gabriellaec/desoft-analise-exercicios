def zera_negativos(lista_valores):
    x = 0
    for i in lista_valores:
        if i < 0:
            lista_valores[x] = 0
        x += 1
    return lista_valores