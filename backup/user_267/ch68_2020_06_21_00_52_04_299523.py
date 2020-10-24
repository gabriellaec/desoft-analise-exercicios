def separa_trios(lista_nomes):
    lista_trios = []
    for i in range(0, len(lista_nomes), 3):
        lista_trios.append(lista_nomes[i:i+3])
    return lista_trios
        