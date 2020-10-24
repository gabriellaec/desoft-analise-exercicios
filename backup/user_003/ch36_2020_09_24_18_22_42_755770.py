def fatorial(n) :
    x=0
    a = n
    resultado =1
    while( n != -1 ):
        resultado = resultado * (n * (n-1))
        x = x+1 
        n = n-1
        
    return resultado

