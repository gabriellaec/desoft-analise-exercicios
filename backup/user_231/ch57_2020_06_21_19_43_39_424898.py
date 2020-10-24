def verifica_progressao(lista):
    print(lista)
    print(len(lista))
    r= lista[1]-lista[0]
    q= lista[1]/lista[0]
    i=1
    PA= True
    PG= True
    while i < len(lista):
        if lista[i]-lista[i-1]!=r:
            PA= False
        if lista[i-1]*q != lista[i]:
            PG= False
        i+=1
    if PA and PG:
        print ('AG')
    if PA:
        print ('PA')
    if PG:
        print ('PG')
    else:
        print( 'NA')
            
    
        
        
        