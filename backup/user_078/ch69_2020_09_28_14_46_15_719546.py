
def junta_listas(lista_de_listas):
    lista_nova = []
    for lista in lista_de_listas:
        for digito in lista:
            lista_nova.append(digito)

    return lista_nova