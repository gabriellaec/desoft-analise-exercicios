def fatorial(n):
    i = 1
    f = 1
    while (i<=n):
        f = f*i
        i = i+1
    return f

print(fatorial(3))