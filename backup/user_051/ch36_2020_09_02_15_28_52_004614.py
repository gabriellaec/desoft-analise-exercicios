def fatorial(n):
    t=1
    while n > 0:
        t*=n
        n-=1
    return t
q=fatorial(4)
print(q)