def fatorial(n):
    i = 1
    y = 0
    while i < n:
        y += y * i
        i += 1
    return y