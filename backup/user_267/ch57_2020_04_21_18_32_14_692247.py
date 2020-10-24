def verifica_progressao(lista):
    for i in range(0,len(lista)-1): 
        if (lista[i+1] - lista[i]) == (lista[i+2] - lista[i+1]) and (lista[i+1]/lista[i]) == (lista[i+2]/lista[i+1]):
            return "AG"
        elif (lista[i+1] - lista[i]) == (lista[i+2] - lista[i+1]) and (lista[i+1]/lista[i]) != (lista[i+2]/lista[i+1]):
            return "PA"
        else:
            return "PG"