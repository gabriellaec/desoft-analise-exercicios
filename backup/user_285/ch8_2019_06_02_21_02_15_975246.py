def verifica_progressao(lista):
    for i in lista:
        if lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            return "PG"
        elif lista[i+1]-lista[i]==lista[i]-lista[i-1]:
            return "PA"
        
        elif lista[i]/lista[i-1]==lista[i+1]/lista[i] and lista[i+1]-lista[i]==lista[i]-lista[i-1]:
            return "AG"
        else:
            return "NA"