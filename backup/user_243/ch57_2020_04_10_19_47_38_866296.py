def verifica_progressao(lista):
    i=0
    while i<len(lista) and len(lista)!="2":
        if lista[i+2]/lista[i+1]==lista[i+1]/lista[i]:
            return ("PG")
        if lista[i+2]-lista[i+1]==lista[i+1]-lista[i]:
            return ("PA")
        else:
            return ("NA")
        i+=1
        
    if len(lista)=="2" and lista[i+2]/lista[i+1]==lista[i+2]-lista[i+1]:
        return ("AG")
        