def fatorial(n):
    x = 1
    for i in range(1,n):
        x = x*i
    return x
print(fatorial(4))