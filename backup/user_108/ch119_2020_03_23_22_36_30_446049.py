def fatorial(n):
    if n <= 2:
        return n
    return n*fatorial(n-1)

def calcula_euler(x,n):
    result = 1
    for i in range(1,n):
        result += x**i/fatorial(i)
    return result