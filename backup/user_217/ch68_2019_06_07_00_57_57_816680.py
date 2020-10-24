def separa_trios (nomes):
    lista_trios = []
    i = 0
    while i < len(nomes):
        lista_trios.append(nomes[i:i+3])
        i += 3 
     return lista_trios    
        
    