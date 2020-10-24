def verifica_progressao(lista):
    PA = True
    PG = True
    n = len(lista)
    i = n - 2
    
    while i <= 1 and PA == True:
        if (lista[i+1] - lista [i]) != (lista [i] - lista [i-1]):
            PA = False
            i = i - 1
        i = n - 2
    while i >=1 and PG == True:
        if 0 in lista:
            PG = False
        elif (lista[i+1] / lista[i]) != (lista [i] / lista[i-1]) and PG == True:
            PG = False
            i= i - 1
        i = n - 2
        
    if PA == True and PG == True:
        return "AG"
    if PA == True:
        return "PA"
    if PG == True:
        return "PG"
    if PA == False and PG == False:
        return "NA"
    
            