def fatorial(x):
    result=1
    for i in range(x):
        result=result*(x-i)
    return result

def calcula_euler(x,n):
    i = 0
    soma = 1+x
    if i < n:
        cosh = (x ** n) / fatorial(n)
        soma += cosh
        i += 1
        
    return soma
