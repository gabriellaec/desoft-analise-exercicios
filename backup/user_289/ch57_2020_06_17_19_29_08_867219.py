def verifica_progressao(lista):
    # Verifica se é PA
    i = 2
    PA = True
    while i <= len(lista):
        razao = abs(lista[1]-lista[0]) 
        if abs(lista[i]-lista[i-1]) == razao:
            i += 1
        else:
            PA = False
            break
    # Verifica se é PG
    i = 2
    PG = True
    while i <= len(lista):
        razao = abs(lista[1]/lista[0]) 
        if abs(lista[i]/lista[i-1]) == razao:
            i += 1
        else:
            PG = False
            break
    if PA == True and PG == True:
        return "AG"
    elif PA == True and PG == False:
        return "PA"
    elif PA == False and PG == True:
        return "PG"
    else:
        return "NA"