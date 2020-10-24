def verifica_progressao(lista):
    i=0
    while i<len(lista):        
        if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            s='PA'       
        elif lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            s='PG'
        elif lista[i+1]-lista[i]==lista[i+2]-lista[i+1] and lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            s='AG'
        else:
            s='NA'
        i+=1
    return s

