def numero_no_indice(lista_numeros):
    lista_nova = []
    i = 0
    while i < len(lista_numeros):
        
        if i == lista_numeros[i]:
            lista_nova.append(lista_numeros[i])
            i += 1

        else:
            i += 1
