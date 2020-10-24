def fatorial(n):
    k = 1
    calculo = 1 
    teste = True
    while teste:
        if n != k:
            calculo = calculo * k
            k = k + 1
            return calculo
        else:
            teste = False
            return calculo
        
    
    