def verifica_progressao(lista):
    print(lista)
    r= lista[1]-lista[0]
    PA= True
    if lista[0]!=0:
        q= lista[1]/lista[0]
        PG= True
    i=1
    while i < len(lista):
        if PA:
            if lista[i]-lista[i-1]!=r:
                PA= False
        if PG:
            if lista[i-1]*q != lista[i]
                PG= False
        i+=1
    if PA and PG:
        print ('AG')
    elif PA:
        print ('PA')
    elif PG:
        print ('PG')
    else:
        print( 'NA')
            
    
        
        
        