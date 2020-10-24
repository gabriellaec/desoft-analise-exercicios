def lista_primos(n):
    
    lista_primos = []
    a = 2
    x = n
    while a<x:
        if x%a == 0:
            x = n -1
            a+=1
        else:
            lista_primos.append(x)
        
            