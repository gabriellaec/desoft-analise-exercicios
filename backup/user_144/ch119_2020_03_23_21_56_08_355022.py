def fatorial(x):
    result=1
    for i in range(x):
        result=result*(x-i)
    return result

def calcula_euler(x,n):
    i = 0
    soma = 1+x
    cosh = (x ** (i)) / fatorial(i)
    while i < n:
        if n <= 2:
            cosh = 0
            soma2 = soma 
        else:
            cosh = (x ** (i)) / fatorial(i)
            soma2 = soma+cosh
        i += 1
        
    return soma2