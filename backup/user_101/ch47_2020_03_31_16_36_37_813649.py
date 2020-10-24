def estritamente_crescente(l):
    if len(l) != 0:
        indice = 1
        while indice < len(l):
            if l[indice] < l[indice - 1]:
                    del l[indice]
                    indice -=1
            indice += 1
        return l
    else:
        return l
            