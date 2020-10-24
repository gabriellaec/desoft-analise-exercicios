def fatorial(n):
    x = n
    cálculo = n
    while x > 0 :
        cálculo *= (n - x) 
        x -= 1
    return (cálculo)
    