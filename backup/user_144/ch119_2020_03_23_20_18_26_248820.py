def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 

def calcula_euler(x,n):
    i = 0
    soma = 0
    if i < n:
        cosh = (x ** n) / fatorial(n)
        soma += cosh
        i += 1
    return 1+soma