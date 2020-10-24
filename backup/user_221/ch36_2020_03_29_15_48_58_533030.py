def fatorial(n):
    s = 1
    x = 1
    while 1 <= x <= n:
        s = s*x
        x = x + 1
    return s       
print(fatorial(4))  