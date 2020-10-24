def verifica_progressao(lista):
    i=1
    while i<len(lista)-1:
        if lista[i+1]-lista[i]==lista[i]-lista[i-1] and lista[i+1]/lista[i]==lista[i]/lista[i-1]:
            resultado='AG'
        elif lista[i+1]-lista[i]==lista[i]-lista[i-1]:
            resultado='PA'
        elif lista[i+1]/lista[i]==lista[i]/lista[i-1]:
            resultado='PG'
        else:
            resultado='NA'
        i+=1
    return resultado