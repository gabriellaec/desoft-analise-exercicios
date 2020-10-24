def numero_no_indice(lista):
    i = 0
    novalista = []
    while i < len(lista):
        if i == lista[i]:
            novalista.append(i)
        i+=1
    return novalista