def verifica_progressao(lista):
    PA = False
    PG = False
    if len(lista) == 0 or 1:
        return 'NA'
    else:
        for i in range(len(lista)-2):
            if lista[i+1]-lista[i] == lista[i+2]-lista[i+1]:
                PA = True
            else:
                PA = False
            if lista[i+1]/lista[i] == lista[i+2]/lista[i+1]:
                PG = True
            else: 
                PG = False
        if PA == True and PG == True:
            return 'AG'
        elif PA == True and PG == False:
            return 'PA' 
        elif PA == False and PG == False:
            return 'NA' 
        elif PG == True and PA == False:
            return 'PG'