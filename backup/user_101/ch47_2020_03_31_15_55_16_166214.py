def estritamente_crescente(l):
    indice = 1
    listaFinal = []
    listaFinal.append(l[0])
    while indice < len(l):
        if l[indice] > l[indice - 1]:
            listaFinal.append(l[indice])
        indice += 1
    return listaFinal
            