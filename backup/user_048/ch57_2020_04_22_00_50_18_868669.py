def verifica_progressao(lista):
    variacao=lista[1]-lista[0]
    variacaog=lista[1]/lista[2]
    PA=True
    PG=True
    for e in range(len(lista)-1):
        if not lista[e+1]-lista[e]==variacao:
            PA=False
        if not lista[e]/lista[e+1]==variacaog:
            PG=False
    if PA and not PG:
        return "PA"
    if PG and not PA:
        return "PG"  
    if PA and PG:
        return "AG"
    if not PA or PG:
        return "NA"