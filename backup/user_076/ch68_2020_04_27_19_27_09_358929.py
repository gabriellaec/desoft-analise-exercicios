def separa_trios (lista_nomes):
    i = 0
    lista_trios = []
    while i+2 < len(lista_nomes):
        trio = [lista[i],lista[i+1],lista[i+2]]
        lista_trios.append(trio)
        i+=3
    return lista_trios