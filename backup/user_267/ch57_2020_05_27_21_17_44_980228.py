def verifica_progressao(lista):
    if len(lista) < 3:
        return "NA"
    pa = True
    pg = True
    for i in range(0,len(lista)-2): 
        if (lista[i+1] - lista[i]) != (lista[i+2] - lista[i+1]):
            pa = False
        if (lista[i+1]/lista[i]) != (lista[i+2]/lista[i+1]):
            pg = False
    if pa and not pg:
        return "PA"
    elif pg and not pa:
        return "PG"
    elif pa and pg:
        return "AG"
    else:
        return "NA"