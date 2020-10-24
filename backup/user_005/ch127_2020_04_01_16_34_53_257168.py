import math
def calcula_elongacao (a, p, w, t):
    x= a*math.cos(math.radians(p)+math.radians(w)*t)
    return x 