def arcotangente (x,n):
    for x in range(-1,1):
        n += x - x**n/n
    return n