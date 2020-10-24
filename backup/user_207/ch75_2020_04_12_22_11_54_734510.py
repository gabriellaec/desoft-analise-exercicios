def verifica_primos (numeros):
    
    dicio ={}
    for n in numeros:
        
        lista_divisores = range(2,n)
        i=0
        resto = 1
        while resto != 0 and i<len(lista_divisores) -1:
            resto = n%lista_divisores[i]
            i+=1
        if resto ==0:
            dicio[n] = False
        else: 
            dicio[n] = True    
        if n == -1:
            dicio[n] = False
        elif n == 0 :
            dicio[n] =  False
        elif n == 1:
            dicio[n] = False   
    
    return dicio
