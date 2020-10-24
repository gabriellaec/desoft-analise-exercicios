'''def fatorial(n):
    i = 1
    produto = 1
    while i <= n:
        produto = produto*i
        i = i+1
    return produto '''

def fatorial(n):
    produto = 1
    for i in range (1, n+1):
        produto *= i
    return produto