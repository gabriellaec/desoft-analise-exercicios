def verifica_progressao(lista):
    PA=True
    PG=True
    base=lista[0]
    razaoPA=lista[1]-lista[0]
    if lista[0]==0:
        PG=False
    else:
        razaoPG=lista[1]/lista[0]
    for numero in lista:
        if numero!=lista[0]:
            if PG:
                if base==0:
                    PG=False
                elif base!=0 and (numero/base)!=razaoPG:
                    PG=False
            if (numero-base)!=razaoPA:
                PA=False
        base=numero
    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return 'NA'