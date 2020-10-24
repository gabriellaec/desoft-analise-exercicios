def calcula_euler(x,n):
    k = 1
    calculax = 1
    calculafatorial = 1
    teste = True
    while teste:
       	if (n+1) > k:
            calculafatorial = calculafatorial * k
            k = k + 1
            
            if x > 0:
                  calculax = calculax + (x**n)/calculafatorial
            else:
                teste = False 
            
    return calculax
