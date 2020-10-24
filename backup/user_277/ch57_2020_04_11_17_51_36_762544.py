def verifica_progressao(lista,PA,PG,NA,AG):
    for i in lista:
        if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            return PA
        elif lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            return PG
        elif lista[i+1]-lista[i]==lista[i+2]-lista[i+1] and lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            return AG
        else:
            return NA