def subtracao_de_listas(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        for n in range(len(lista2)):
            if not i in n:
                lista3.append(i)		
    return lista3