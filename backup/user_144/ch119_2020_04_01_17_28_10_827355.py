def fatorial(x):
    result=1
    for i in range(x):
        result=result*(x-i)
    return result

def calcula_euler(x,n):
    soma = 0
    for i in n:
        soma += (x ** (i)) / fatorial(i)       
        
    return soma