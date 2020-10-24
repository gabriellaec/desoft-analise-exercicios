def numero_no_indice(lista_indice):
    i = 0
    lista2 = []
    while i < len(lista_indice):
        lista2 = []
        if i == lista_indice[i]:
            lista2.append(lista[i])
        i=i+1
    return lista2