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
    if n == 1:
        return 1
    if n == 2:
        a = 1 + x
        return a
    i = 2
    somas = 0
    while i < n:
        s = (x**i)/fatorial(i)
        somas = somas + s
        i += 1
        b = 1 + x + somas
    return b
    
        
    
    