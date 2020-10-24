def verifica_primos(listanumeros):
    primos = {}
    for i in listanumeros:
        if i == 0:
            primos[i] = False
            
        elif i == 1:
            primos[i] = False
        
        elif i == 2:
            primos[i] = True
    
        else:
            divisor = 3
            while divisor < i:
                if i%2 == 0:
                    primos[i] = False
                    divisor+=2
                else:
                    if i==divisor:
                        primos[i] = False
                        divisor+=2 
                    
                    if i%divisor == 0:
                        primos[i] = False
                        divisor+=2 
                    else:
                        divisor +=2 
    return primos