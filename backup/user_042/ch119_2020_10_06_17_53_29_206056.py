def fatorial(m):
    if m == 0:
        return 1
    i = 1 
    acumulador = 1
    while i <=m:
        a = i * 1 
        acumulador = acumulador * a
        i += 1
    return acumulador
def calcula_euler(x, n):
    if x == 0:
        return 1
    i = 1
    soma = 0
    while i < (n -1):
        acumula = (x**i)/fatorial(n)
        soma = soma + acumula
        i += 1
        y = 1 + acumula
    return y
        
    
    