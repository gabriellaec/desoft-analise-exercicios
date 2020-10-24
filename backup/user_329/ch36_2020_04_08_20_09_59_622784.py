def fatorial(n):
    x = 1
    n! = 0
    y = (n-x)
    while y > 0:
        n! = n*y
        n! += n!
        x += 1
    return n!