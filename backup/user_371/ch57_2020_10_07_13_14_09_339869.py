def verifica_progressao(lista):
    i=len(lista)-2
    PG=True
    PA=True
    while i>=0:
        if lista[i-1]==0 and lista[i]!=lista[i-1]:
            return "NA"
            i=-1
        divisao_inicial=lista[len(lista)-1]/lista[len(lista)-2]
        subtracao_inicial=lista[len(lista)-1]-lista[len(lista)-2]
        divisao=lista[i]/lista[i-1]
        subtracao=lista[i]-lista[i-1]

        i-=1

        if subtracao!=subtracao_inicial:
            PA=False
        if divisao_inicial!=divisao:
            PG=False
        if PA == False and PG == False and i==0:
            return "NA"
        elif PA == True and PG == False and i==0:
            return "PA"
        elif PA == False and PG == True and i==0:
            return "PG"
        elif PA == True and PG == True and i==0:
            return "AG"