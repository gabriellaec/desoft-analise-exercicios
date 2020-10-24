def subtracao_listas(lista1, lista2):
    for i in lista1:
        for j in lista2:
            a =type(i)
            b =type(j)
            if a == b:
                if i == j:
                    lista1.remove(i)
    return lista1