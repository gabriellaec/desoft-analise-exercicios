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
    n = f**x
     resposta = n
    if n == 1:
        return 1
    if n == 2:
        a = 1 + x
        return a
    i = 2
    while i < n:
        somas = (x**i)/fatorial(i)
        somas += somas
        i += 1
    b = 1 + x + somas
    return b
    
        
    
    