def raiz_quadrada(n):
    time = 0
    
    contador = 1
    y = True

    while y:
        n = n - contador
        
        time = time + 1
        
        print('Contador:', contador)
        
        
        if n == 0:
            y = False
            return(time)

        contador = contador + 2