'''def fatorial(n):
    i = 1
    produto = 1
    while i <= n:
        produto = produto*i
        i = i+1
    return produto '''

def fatorial(n):
    produto = 1
    for i in range (n+1):
        produto = produto*i
    return produto