
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
                elif i % divisor == 0:
                    primos[i] = True
                    divisor+=2
                else:
                    primos[i]=True
                    divisor+=2
    return primos
                   