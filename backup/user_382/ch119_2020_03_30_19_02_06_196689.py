def fatorial(n):
    produto = n 
    t = 1 
    while n > t:
        produto = produto * (n-t)
        t += 1 
    return produto 

def calcula_euler(n,x):
    soma = 1 + x
    for i in range(2,n):
        soma += (x**i)/fatorial(i)
    return soma 