def verifica_progressao(s):
    i=0
    while i<len(lista):        
        if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            s='PA'       
        elif lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            s='PG'
        elif lista[i+1]-lista[i]==lista[i+2]-lista[i+1] and lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            s='AG'
        elif lista[i+1]-lista[i]!=lista[i+2]-lista[i+1] and lista[i+1]/lista[i]!=lista[i+2]/lista[i+1]:
            s='NA'
        i+=1
    return s
