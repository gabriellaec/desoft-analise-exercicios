def eh_crescente (lista):
    if lista == []:
        return False
    if len(lista) == 1:
        return True
    lista_c = []
    lista_c.append(lista[0])
    c = lista[0]
    for i in range(len(lista)):
        if lista[i] > c:
            c = lista[i]
            lista_c.append(c)
    if lista == lista_c:
        return True
    else:
        return False