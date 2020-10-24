def junta_listas (lista_de_listas):
    lista_final = []
    for i in range(len(lista_de_listas)):
        lista = lista_de_listas[i]
        for e in range(len(lista)):
            elemento = lista[e]
            lista_final.append(elemento)
    return lista_final