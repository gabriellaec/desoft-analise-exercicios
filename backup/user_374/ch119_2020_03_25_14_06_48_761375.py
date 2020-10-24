
def calcula_euler(x,n):
    k = 1
    calcula_x = 1
    calcula_fatorial = 1
    teste = True
    while teste:
       	if (n+1) > k:
            calcula_fatorial = calcula_fatorial * k
            if x > 0:
                  calcula_x = calcula_x + (x**k)/calcula_fatorial
            else:
                teste = False
            k = k + 1    
        else:
            teste = False
    return calcula_x

