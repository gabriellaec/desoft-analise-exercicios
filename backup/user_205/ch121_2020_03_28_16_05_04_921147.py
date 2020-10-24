def subtracao_de_listas(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        for i in range(len(lista2)):
            if not lista1[i] in lista2:
                lista3.append(lista1[i])		
    return lista3