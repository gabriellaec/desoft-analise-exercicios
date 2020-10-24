def junta_listas(lista_listas):
    unica = []
    i = 0
    while i < len(lista_listas):
        if len(lista_listas[i]) == 1:
            unica.append(lista_listas[i][0])

        if len(lista_listas[i]) != 1:
            j = 0
            while j < len(lista_listas[i]):
                unica.append(lista_listas[i][j])
                j += 1
        i += 1
            
        
    return unica