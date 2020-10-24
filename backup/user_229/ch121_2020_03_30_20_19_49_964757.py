def subtracao_de_listas(lista1, lista2):
    lista1 = [2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    lista3 = []
    i = 0
    while i < len(lista1):
        while lista1[i] not in lista2:
            lista3.append(lista1[i])
        i += 1
    return lista3