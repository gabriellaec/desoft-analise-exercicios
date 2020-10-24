def numero_do_indice(l):
    indice = 0
    listaFinal = []
    while indice < len(l):
        if indice == l[indice]:
            listaFinal.append(l[indice])
        indice += 1
    return listaFinal