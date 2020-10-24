def estritamente_crescente(lista):
    novalista = []
    i = 0
    novalista.append(lista[0])
    while i < len(lista):
        maiorelemento = lista[0]
        if lista[i]>maiorelemento:
            maiorelemento = lista[i]
            novalista.append(maiorelemento)
        i+=1
    return novalista