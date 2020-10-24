def separa_trios (lista_nomes):
    i=0
    lista_trios = []
    while i< len(lista_nomes):
        
        lista_trios.append(lista_nomes[i:i+3])
        i+= 3
    return lista_trios