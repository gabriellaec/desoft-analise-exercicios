def separa_trios (lista_nomes):
    i = 2
    lista_trios = []
    while i < len(lista_nomes) - 1:
        lista_trios.append([lista_nomes[i-2] + ', ' + lista_nomes[i-1] + ', ' + lista_nomes[i]])
        i += 3
        if len(lista_nomes) % 3 != 0:
            lista_trios.append()
    return lista_trios