#solução1
def fatorial(n):
    x = 1
    i = 2
    while i <= n:
        x = x*i
        i = i + 1
    return x


#solução2
def fatorial(n):
    soma=1
    for i in range(1,n+1):
        soma=soma*i
    return soma
        