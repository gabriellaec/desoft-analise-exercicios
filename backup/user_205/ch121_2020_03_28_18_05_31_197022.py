def subtracao_de_listas(lista1,lista2):
    lista3 = []
    for i in lista1:
        for n in lista2:
            if i==n:
                pass
            else:
                lista3.append(i)
    return lista3