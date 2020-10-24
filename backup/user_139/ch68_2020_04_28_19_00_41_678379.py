def separa_trios (lista_nomes):
    lista_trios = []
    i = 0
    while i < len(lista_nomes):
        lista_trios.append(lista_nomes[i:i+3])
        i += 3
    return lista_trios