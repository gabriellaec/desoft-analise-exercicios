def fatorial(n):
    x = 1
    n1 = 0
    y = (n-x)
    while y > 0:
        z = n*y
        n1 += z
        x += 1
    return n1