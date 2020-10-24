def numero_no_indice(l1):
    novalista = []
    for i in range(0,len(l1)):
        if l1[i] == i:
            novalista.append(l1[i])

    return novalista