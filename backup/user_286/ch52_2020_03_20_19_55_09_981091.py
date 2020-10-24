def calcula_total_da_nota(lista_valores, lista_quantidade):
    lista_total = []
    for item in lista_valores:
        lista_total.append(float(lista_valores[lista_valores.index(item)])*float(lista_quantidade[lista_valores.index(item)]))

    return lista_total