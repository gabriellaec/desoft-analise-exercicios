def verifica_progressao(sequencia):
    razao=sequencia[1]-sequencia[0]
    for i in range(1,len(sequencia)):
        PA=True
        if sequencia[i]-sequencia[i-1]!=razao:
            PA=False
            break
    if sequencia[0]==0:
        PG=True
        for numero in sequencia:
            if numero!=0:
                PG=False
                break
    else:
        quociente=sequencia[1]/sequencia[0]
        if quociente==0:
            PG=True
            for i in range(1,len(sequencia)):
                if sequencia[i]!=0:
                    PG=False
                    break
        else:
            for numero in sequencia:
                if numero==0:
                    PG=False
                else:
                    for i in range(1,len(sequencia)):
                        PG=True
                        if sequencia[i]/sequencia[i-1]!=quociente:
                            PG=False
                            break
    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG:
        return 'PG'
    else:
        return 'NA'