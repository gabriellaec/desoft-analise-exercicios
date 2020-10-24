def estritamente_crescente(lista):
    novalista = []
    i = 0
    novalista.append(lista[0])
    maiorelemento = lista[i]
    while i < len(lista):
        if lista[i]>maiorelemento:
            maiorelemento = lista[i]
            novalista.append(maiorelemento)
        i+=1
    return novalista