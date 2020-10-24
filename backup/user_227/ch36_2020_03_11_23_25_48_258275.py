def fatorial(n):
    x = n - 1
    cálculo = n
    while x > 0 :
        cálculo *= (n - x) 
        x -= 1
    return (cálculo)
    