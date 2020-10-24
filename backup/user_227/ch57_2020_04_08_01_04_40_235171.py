def verifica_progressao(lista):
    razaoPA=lista[1]-lista[0]
    razaoPG=lista[1]/lista[0]
    PA=True
    PG=True
    for numero in lista:
        if numero==lista[0]:
            base=numero
        else:
            if (numero/base)!=razaoPG:
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