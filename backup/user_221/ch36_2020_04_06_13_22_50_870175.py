def fatorial(n):
    s = 1
    for x in range(1, n+1):
        s = s*x
    return s     
print(fatorial(4))  