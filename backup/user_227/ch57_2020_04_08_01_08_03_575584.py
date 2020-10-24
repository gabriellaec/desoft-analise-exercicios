def verifica_progressao(lista):
    razaoPA=lista[1]-lista[0]
    if lista[0]!=0:
        razaoPG=lista[1]/lista[0]
    PA=True
    PG=True
    for numero in lista:
        if numero==lista[0] and numero!=0:
            base=numero
        elif numero!=lista[0] and numero!=0:
            if (numero/base)!=razaoPG and numero!=0:
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