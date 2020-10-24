def verifica_progressao(lista):
    PA = False
    PG = False
    AG = False
    n = len(lista)
    i = n - 2
    if n <= 2:
        return "AG"
    while i >= 1:
        if (lista[i+1] - lista[i]) == (lista [i] - lista[i-1]) and (lista[i+1] / lista[i]) == (lista [i] / lista[i-1]):
            AG = True
            i = i - 1
        elif (lista[i+1] / lista[i]) == (lista [i] / lista[i-1]):
            PG = True
            i = i - 1
        elif (lista[i+1] - lista[i]) == (lista [i] - lista[i-1]):
            PA = True
            i = i - 1
        else:
            AG = False
            PG = False
            PA = False
            i = i - 1
    if AG == True:
        return "AG"
    elif PG ==True:
        return "PG"
    elif PA == True:
        return "PA"
    else: 
        return "NA"