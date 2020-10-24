import math
def calcula_elongacao (A, o, w, t):
    return A*math.cos(math.radians(o) + math.radians(w)*t)