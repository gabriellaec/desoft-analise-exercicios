def fatorial(n):
    i = 2
    y = 0
    while i < n:
        y += y * i
        i += 1
    return y