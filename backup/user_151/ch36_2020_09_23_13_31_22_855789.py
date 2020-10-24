def fatorial(n):
    y = 1
    while True:
        if n != 0:
            y = y * n
            n = n-1
        else:
            break
    return y