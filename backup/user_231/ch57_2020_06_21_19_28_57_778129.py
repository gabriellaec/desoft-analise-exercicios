def verifica_progressao(lista):
    print(lista)
    print(len(lista))
    r= lista[1]-lista[0]
    i=1
    PA= True
    PG= True
    while i < len(lista):
        if lista[i]-lista[i-1]!=r:
            PA= False
        if lista[i-1]*r != lista[i]:
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
            
    
        
        
        