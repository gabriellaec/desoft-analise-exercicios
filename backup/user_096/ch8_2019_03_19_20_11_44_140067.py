def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if (lista[i]+lista[i+2])/2==lista[i+1]:
            return"PA"
        elif (lista[i]*lista[i+2])**0.5==lista[i+1]:
            return"PG"
        elif (lista[i]+lista[i+2])/2==lista[i+1] and (lista[i]*lista[i+2])**0.5==lista[i+1]:
            return"AG"
        else:
            return"NA"
        i+=1