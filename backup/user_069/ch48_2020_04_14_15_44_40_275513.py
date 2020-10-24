def eh_crescente (lista):
    lista_c = []
    lista_c.append(lista[0])
    c = lista[0]
    for i in range(len(lista)-1):
        if lista[i] > c:
            c = lista[i]
            lista_c.append(c)
    if lista == lista_c:
        return True
    else:
        return False