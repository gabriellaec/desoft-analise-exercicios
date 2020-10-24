def verifica_progressao(lista):
    r= lista[1]-lista[0]
    i=0
    PA= True
    PG= True
    while i < len(lista):
        if lista[i+1]-lista[i]!=r:
            PA= False
            
        if lista[i]*r != lista[i+1]:
            PG= False
        i+=1
    if PA and PG:
        return 'AG'
    if PA:
        return 'PA'
    if PG:
        return 'PG'
    else:
        return 'NA'
            
    
        
        
        