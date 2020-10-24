def estritamente_crescente(l):
    if len(l) != 0:
        indice = 1
        listaFinal = []
        listaFinal.append(l[0])
        while indice < len(l):
            if l[indice] > l[indice - 1]:
                listaFinal.append(l[indice])
            indice += 1
        return listaFinal
    else:
        return l
            