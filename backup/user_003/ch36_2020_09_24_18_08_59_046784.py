def fatorial(n) :
    x=0
    a = n
    while(x < a+1 ):
        resultado = n * (n-1)
        x = x+1 
        n -= n
        
    return resultado

