def fatorial(n):
    resultado=1
    conta=1
    
    
    while conta<=n:
        resultado*=conta
        conta+=1
    return resultado
def calcula_euler(x,n):
    i=1
    contad=1
    
    while i<n:
        contad=contad+(x**i)/fatorial(i)
        i+=1
    return contad