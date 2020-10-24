def verifica_progressao(lista):
    if lista[0]>0:
         variacao=lista[1]-lista[0]
         variacaog=lista[1]/lista[0]
    else:
        variacao=lista[2]-lista[1]
        variacao=lista[2]/lista[1]
    PA=True
    PG=True
    for e in range(len(lista)-1):
        if not lista[e+1]-lista[e]==variacao:
            PA=False
        if not lista[e+1]/lista[e]==variacaog:
            PG=False
    if PA and not PG:
        return "PA"
    if PG and not PA:
        return "PG"  
    if PA and PG:
        return "AG"
    if not PA or PG:
        return "NA"