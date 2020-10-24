def estritamente_crescente(lista):
    soh_crescente = []
    i = 0
    while i<len(lista):
        if lista[i]<lista[i+1]:
            soh_crescente.append(lista[i])
        i += 1
    return soh_crescente