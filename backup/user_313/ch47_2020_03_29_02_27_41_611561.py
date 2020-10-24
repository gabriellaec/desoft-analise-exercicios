def estritamente_crescente(lista):
    dados = lista
    c = len(lista)
    contador = 1
    contador2 = 0
    novalista = [0]*1
    novalista[0] = dados[0]*1

    while c != contador:
        if lista[contador]>novalista[contador2]:
            novalista.insert(contador,lista[contador])
            contador = contador + 1
            contador2 = contador2 +1

        else: 
            contador = contador + 1
       
           
    return novalista

