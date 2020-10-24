def estritamente_crescente(lista):
    c = len(lista)
    contador = 1
    contador2 = 0
    novalista = [0]*c
    novalista[0] = lista[0]
    while c != contador:
        if lista[contador]>novalista[contador2]:
            novalista.insert(contador,lista[contador])
            contador = contador + 1
            contador2 = contador2 +1

        else: 
            contador = contador + 1
           
    return novalista
