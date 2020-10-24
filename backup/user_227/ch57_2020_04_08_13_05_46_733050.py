def verifica_progressao(lista):
    PA=True
    PG=True
    razaoPA=lista[1]-lista[0]
    if lista[0]==0:
        PG=False
    else:
        razaoPG=lista[1]/lista[0]
    for numero in lista:
        base=numero
        if numero!=lista[0]:
            if base==0 :
                PG=False
            if (numero-base)!=razaoPA:
                PA=False
    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return 'NA'