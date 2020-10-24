def junta_listas(lista):
    lista_nova = []
    i = 0
    while i<len(lista):
        j = 0
        lista_na_lista = lista[i]
        while j<len(lista_na_lista):
            lista_nova.append(lista_na_lista[j])
            j+=1
        i+=1
    return lista_nova
            