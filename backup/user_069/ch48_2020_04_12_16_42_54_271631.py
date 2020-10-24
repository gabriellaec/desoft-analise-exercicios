def eh_crescente (lista):
    if lista == [] and len(lista) == 1:
        return True
    lista_crescente = []
    lista_crescente.append(lista[0])
    c = len(lista) - 1
    i_l = 1
    i_lc = 0
    while c != i_l:
        if lista[i_l] > lista_crescente[i_lc]:
            lista_crescente.append(lista[i_l])
            i_l += 1
            i_lc += 1
        else:
            i_l += 1
    if lista_crescente == lista:
        return True
    else:
        return False