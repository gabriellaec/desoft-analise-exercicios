def arcotangente (x, n):
    o = 1
    sin = 1
    g = 0
    while i<n*2:
        p = sin *(x**i)/i
        i = i + 2
        g = g + p
        sin = -sin
    return x