def fatorial(n):
    resultado=1
    conta=1
    
    
    while conta<=n:
        resultado*=conta
        conta+=1
    return resultado
def calcula_euler(x,n):
    i=1
    conta=1
    
    while i<n:
        conta=conta+(x**i)/factorial(i)
        i+=1
    return conta