def fatorial(n):
    
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado


def calcula_euler(x, n):
    
    ex = 0
    
    for i in range(n):
        ex += (x ** i)/fatorial(i)
    
    return ex
    