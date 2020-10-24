def verifica_progressao(lista):
    a = len(lista)
    c = 0
    b = 0
    
    for i in range(1, (a-1)):
        if c > a:    
            print(lista[i])
            if (lista[i] ** 2) == lista[i - 1] * lista[i+1]:
                
                c+=1
                PG = True
                
            else:
                PG = False
                c = a + 1   


    for i in range(1, (a-1)):
        while b < a:     
            print(lista[i])
            if lista[i] == (lista[i - 1] + lista[i+1])/2:
                
                b+=1
                PA = True

            else:
                b = a + 1
                PA = False
            
    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG :
        return 'PG'
    else:
        return 'NA'
