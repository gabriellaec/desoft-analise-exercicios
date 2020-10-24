def verifica_progressao(lista):
    i = 1
    PA = True
    PG = True
    while i <= len(lista):
        if lista[i+1] - lista[i] != lista[i+2] - lista[i+1]:
            PA = False
        elif lista[i+1]/lista[i] != lista[i+2]/lista[i+1]:
            PG = False
        i+=1
    if PA and PG:
        return "AG"
    elif not PA and not PG:
        return "NA"
    