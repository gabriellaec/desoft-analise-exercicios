def verifica_progressao(lista):
    i=0
    r = lista[0]-lista[1] 
    q = lista[0]/lista[1]
    while i<=len(lista):
        if lista[i]+r == lista[i+1] and lista[i]*q == lista[i+1]:
            return ("AG")
        if lista[i]+r == lista[i+1]:
            return ("PA")
        if lista[i]*q == lista[i+1]:
            return("PG")
        else:
            return ("NA")
    i+=1