import math
def calcula_euler (n):
    x = 1
    n = 1
    while x <= n:
        y = 1 + y**x/math.factorial(x)
        x += 1
        return y
        