def fatorial(n):
    i= n-2
    resultado=0
    while i-1>=0:
        resultado= n*(n-1)**i
        i= i-1
    if i==0:
        return resultado
    
        
        
