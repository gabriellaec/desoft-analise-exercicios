def fatorial(n):
    x = 1
    n1 = 0
    y = (n-x)
    while y > 0:
        n1 = n*y
        n1 += n1
        x += 1
    return n1