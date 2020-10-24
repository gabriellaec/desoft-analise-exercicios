def separa_trios (lista_nomes):
    
    i = 0
    lista_trios = []
    while i < len(lista_nomes):
        nomes = lista_nomes[i:i+3]
        lista_trios.append(nomes)
        i += 3
        
    return lista_trios
        