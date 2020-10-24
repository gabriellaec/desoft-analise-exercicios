def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if lista[i+2]/lista[i+1]==lista[i+1]/lista[i]:
            return ("PG")
        if lista[i+2]-lista[i+1]==lista[i+1]-lista[i]:
            return ("PA")
        if lista[i+2]/lista[i+1]==lista[i+2]-lista[i+1]:
            return ("AG")
        else:
            return ("NA")
        i+=1
        