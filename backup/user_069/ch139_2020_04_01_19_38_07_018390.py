import math
def arcotangente (x,n):
    i = 0
    s = 0
    while i < n:
        s += x**i/i
        i += 2
    return math.radians(s)