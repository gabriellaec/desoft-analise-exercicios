def raiz_quadrada(n):
    time = 0
    
    contador = 1
    y = True

    while contador <= n:
        n = n - contador
        
        
        
        print('Contador:', contador)
        
        
        if n == 0:
            y = False
        
        contador = contador + 2
        time = time + 1
    
    return(time)