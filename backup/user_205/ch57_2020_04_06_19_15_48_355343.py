def verifica_progressao(lista):
    for i in range(len(lista-2)):
        if ((lista[i]+lista[i+2])/2 == lista[i+1]):
            return "PA"
        elif (lista[i+1]**2 == lista[i]*lista[i+2]):
            return "PG"
        elif ((lista[i]+lista[i+2])/2 == lista[i+1] and lista[i+1]**2 == lista[i]*lista[i+2]):
            return "AG"
        else:
            return "NA"