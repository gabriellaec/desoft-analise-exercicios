def verifica_progressao(lista):
    i = 0
    while i<len(lista):
        if r == lista[i+1]-lista[i]:
            return "PA"
        if lista[i+1]-lista[i] == lista[i+1]/lista[i]:
            return "AG"
        elif q == lista[i+1]/lista[i]:
            return "PG"
        else:
            return "NA"
        i+=1