def verifica_progressao(lista):
    i = 0
    PA = True
    PG = True
    while i < len(lista)-2:
        if lista[i+1] - lista[i] != lista[i+2] - lista[i+1]:
            PA = False
        if lista[i+1]==0 or lista[i]==0 or lista[i+1]/lista[i] != lista[i+2]/lista[i+1]:
            PG = False
        i+=1
    if PA and PG:
        return "AG"
    elif not PA and not PG:
        return "NA"
    elif PA:
        return "PA"
    else:
        return "PG"
    