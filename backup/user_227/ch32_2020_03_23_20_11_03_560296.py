def lista_primos(x) :
    
    lista = [0]*x
    lista[0] = 2
    i = 1
    ímpares = 3
    while i < x:
        if (lista[i-1] + 1) % 2 != 0 :
                
            if ímpares < (lista[i-1] + 1) :
                
                while (lista[i-1] + 1) % ímpares != 0:
                    ímpares += 2