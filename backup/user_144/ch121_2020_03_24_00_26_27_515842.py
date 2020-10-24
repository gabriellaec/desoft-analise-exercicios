def subtracao_de_listas(lista1,lista2):
    new_list = []
    for e in range(len(lista1)):
        if lista1[e] not in lista2:
            new_list.append(lista1[e])
        elif lista2 == []:
            new_list = lista1
                
    return new_list