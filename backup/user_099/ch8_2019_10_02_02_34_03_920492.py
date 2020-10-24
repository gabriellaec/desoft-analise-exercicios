def verifica_progressao(sequencia):
    razao=sequencia[1]-sequencia[0]
    for i in range(1,len(sequencia)):
        PA=True
        if sequencia[i]-sequencia[i-1]!=razao:
            PA=False
            break
    quociente=sequencia[1]/sequencia[0]
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