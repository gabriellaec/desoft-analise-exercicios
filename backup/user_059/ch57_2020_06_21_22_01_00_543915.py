def verifica_progressao(lista):
    PA = True
    PG = True
    for i in range(len(lista)-2):
        if lista[i+1]-lista[i] == lista[i+2]-lista[i+1]:
            pass
        else:
            PA = False
        if lista[i+1]/lista[i] == lista[i+2]/lista[i+1]:
            pass
        else: 
            PG = False
    if PA == False and PG == False:
        return 'NA' 
    if PA == True and PG == True:
        return 'AG'
    if PA == True and PG == False:
        return 'PA' 
    if PG == True and PA == False:
        return 'PG'