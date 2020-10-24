def fatorial (n):
    i = n-1

    while i >= 1:
        x = n*i
        i -= 1
        n = x
    return n

