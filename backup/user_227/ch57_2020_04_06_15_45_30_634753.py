def verifica_progressao(lista):   
    razaoPA=lista[1]-lista[0]
    razaoPG=lista[1]/lista[0]
    i=0
    while i<len(lista):
        PA=True
        PG=True
        razao1=lista[i+1]-lista[i]
        razao2=lista[i+1]/lista[i]
        if razao1!=razaoPA:
            PA=False
        if razao2!=razaoPG:
            PG=False
        i+=1
    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return 'NA'