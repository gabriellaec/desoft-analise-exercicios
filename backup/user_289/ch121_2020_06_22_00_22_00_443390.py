def subtracao_de_listas(lista1, lista2):
    lista3 = []
    for elemento in lista1:
        if elemento not in lista2:
            lista3.append(elemento)
    return lista3