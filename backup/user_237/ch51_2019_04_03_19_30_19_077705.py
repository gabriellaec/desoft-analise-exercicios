def estritamente_crescente(lista):
    crescente = []
    i = 0
    for e in lista:
        if e == lista[0]:
            crescente.append(e)
            i += 1
        else:
            if e > crescente[1]:
                crescente.append(e)
                i+= 1
    return crescente