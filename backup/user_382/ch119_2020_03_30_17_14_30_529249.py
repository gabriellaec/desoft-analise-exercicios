def fatorial(n):
    produto = n 
    t = 1 
    while n > t:
        produto = produto * (n-t)
        t += 1 
    return produto 
def calcula_euler(n,x):
    soma = 1 + x
    for i in range(1,n-1):
        soma += (x**(i))/fatorial(i)
        i -= 1
    return soma 
        