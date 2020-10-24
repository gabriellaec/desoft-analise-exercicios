def fatorial(n):
    produto = n 
    t = 1 
    while n > t:
        produto = produto * (n-t)
        t += 1 
    return produto 

def calcula_euler(n,x):
    soma = 1 
    if n == x:
        for i in range(1,n):
            soma += (x**(i))/fatorial(i)
    soma = 1 + x
    if n!= x:
        for i in range(2,n):
            soma += (x**(i))/fatorial(i)
        
    return soma 
        