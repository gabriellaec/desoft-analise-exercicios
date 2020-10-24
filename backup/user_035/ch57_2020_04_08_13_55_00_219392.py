def verifica_progressao(lista):
    pa = True
    pg = True
    
    if len(lista) < 2:
        return "NA"
    elif len(lista) == 2:
        return "AG"
    indice_pa = lista[1]-lista[0]
    
    if lista[0] == 0 and lista[1] == 0:
        indice_pg = 0
    elif lista[0] == 0 or lista[1] == 0:
        pg = False
    else:
        indice_pg = lista[1]/lista[0]
    
    i=1
    while i < len(lista)-1:
        if lista[i+1]-lista[i]!= indice_pa:
            pa = False
            break
        i += 1
        
    i = 1
    while pg and i < len(lista)-1:
        if lista[i+1] == 0:
            if  indice_pg != 0:
                pg = False
        elif lista[i+1]/lista[i] != indice_pg:
            pg = False

        i += 1
    if pa and pg:
        return "AG"
    elif pa:
        return "PA"
    elif pg:
        return "PG"
    else:
        return "NA"