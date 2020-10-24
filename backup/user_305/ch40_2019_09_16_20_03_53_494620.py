def fatorial(n):
    i = 0
    y = 1
    while i < n:
        y += y * i
        i += 1
    return y