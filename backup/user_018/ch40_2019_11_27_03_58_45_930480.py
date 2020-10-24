n = 7

def fatorial(n):
    resultado = 1
    while n != 1:
        resultado *= n
        n-=1
    return resultado

print(fatorial(n))