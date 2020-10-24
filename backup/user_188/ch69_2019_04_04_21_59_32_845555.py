def junta_listas(lista_composta):
    lista_final = []
    for lista in lista_composta:
        for numero in lista:
            lista_final.append(numero)
    return lista_final