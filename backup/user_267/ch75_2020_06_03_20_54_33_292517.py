def verifica_primos(listan):
    dicio = dict()
    for n in listan:
        dicio[n]= True
        if (n <= 1):
            dicio[n]= False
        elif n == 2:
            dicio[n]= True
        else:
            i = n-2
            if n % 2 == 0:
                dicio[n]= False
            while i>1:
                if n % i == 0:
                    dicio[n]= False
                i -= 2
                if i == 0:
                    dicio[n]= False
            
    return dicio

