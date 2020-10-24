import math
def snell_descartes (n1, n2, x):
    sin_x = math.sin(math.radians(x))
    q = n2 * sin_x * n1
    sin_y = math.sin(math.radians(q))
    return sin_y
    