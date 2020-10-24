def verifica_progressao(lista):
    a = (lista[i+1] - lista[i]) == (lista[i+2] - lista[i+1])
    b = (lista[i+1]/lista[i]) == (lista[i+2]/lista[i+1])
    for i in range(0,len(lista)-1): 
        if a and not b:
            return "PA"
        elif b and not a:
            return "PG"
        elif a and b:
            return "AG"
        else:
            return "NA"