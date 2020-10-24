def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        y = fat*i/(n+1)*i
        i += 1
        return y
