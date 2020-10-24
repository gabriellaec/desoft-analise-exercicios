def subtracao_de_listas(lista1,lista2):
    for item in lista1:
        if item in lista2:
            lista2.remove(item)
    return lista2