def calcula_euler(x,n):
    k = 1
    calculo_x = 1
    calculo_fatorial = 1
    teste = True
    while teste:
       	if (n+1) > k:
            calcula_fatorial = calcula_fatorial * k
            k = k + 1
            
            if x > 0:
                  calcula_x = calcula_x + (x**n)/calcula_fatorial
			else:
                test = False 
            
    return calculo

