def verifica_progressao(a):
    listaPA = []
    listaPG = []
    i = 0
    k = 0
    while i+1 < len(a):
        PG = a[i+1] / a[i]
        listaPG.append(PG)
        i += 1
    while k+1 < len(a):
        PA = a[k+1] - a[k]
        listaPA.append(PA)
        k += 1
    if max(listaPG) == min(listaPG) and max(listaPA) == min(listaPA):
        return "AG"
    elif max(listaPG) == min(listaPG):
        return "PG"
    elif max(listaPA) == min(listaPA):
        return "PA"
    else:
        return "NA"
        
    
    