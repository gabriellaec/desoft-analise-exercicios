def calcula_euler (n):
    x = 0
    n = 0
    while x < n:
        y = y**x/math.factorial(x)
        x += 1
        return y
        