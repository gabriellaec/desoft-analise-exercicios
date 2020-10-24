def estritamente_crescente(lista_numeros):
    lista_nova = []
    i1 = 0  
    i2 = 1

    while i2 < len(lista_numeros):
        if lista_numeros[i1] < lista_numeros[i2]:

            if lista_numeros[i1] in lista_nova:
                i1 += 1
                i2 += 1

            else:
                lista_nova.append(lista_numeros[i1)
                i1 += 1
                i2 += 1 

    return lista_nova