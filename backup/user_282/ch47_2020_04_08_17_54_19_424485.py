def estritamente_crescente(lista):
    soh_crescente = list()
    i = 0
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            soh_crescente.append(lista[i])
    return soh_crescente