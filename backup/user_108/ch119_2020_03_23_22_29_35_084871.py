def fatorial(n):
    if n <= 1:
        return n
    return n*fatorial(n-1)

def calcula_euler(x,n):
	result = 1
    for i in range(1,n):
        result += x**n/fatorial(n)
    return result