def calcula_euler(x,n):
    import math
    i=1
    euler = 1
    while i < n:
        euler = euler + x**i/math.factorial(i)
        i=i+1
    return euler