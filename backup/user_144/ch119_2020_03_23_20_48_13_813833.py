def fatorial(x):
    result=1
    for i in range(x):
        result=result*(x-i)
    return result

def calcula_euler(x,n):
    i = 0
    soma = 1+x
    if i < n:
        if n <= 2:
            cosh = 0
        else:
            cosh = (x ** (n-1)) / fatorial(n-1)
            
        soma += cosh
        i += 1
        
    return soma