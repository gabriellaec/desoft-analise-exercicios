def verifica_progressao(lista):
    i=0
    x=lista[i+1]-lista[i]
    y=lista[i+1]/lista[i]
    while i+2<len(lista):        
        if x==lista[i+2]-lista[i+1] and y==lista[i+2]/lista[i+1]:
            s='AG'
        elif x==lista[i+2]-lista[i+1]:
            s='PA'       
        elif  y==lista[i+2]/lista[i+1]:
            s='PG'
        else:
            s='NA'
        i+=1
    return s

