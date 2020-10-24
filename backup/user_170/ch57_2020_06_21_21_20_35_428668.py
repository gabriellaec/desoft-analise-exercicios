def verifica_progressao(numeros):
    q = numeros[1]/numeros[0]
    sub = numeros[1]-numeros[0]
    for n in range(len(numeros)):
        if numeros[n+1]/numeros[n] != q:
            PG = False
    for n in range(len(numeros)):
        if numeros[n+1]-numeros[n] != sub:
            PA = False
    if PG == True and PA == True:
        return "AG"
    if PG == True:
        return "PG"
    if PA == True:
        return "PA"
    else:
        return "NA"