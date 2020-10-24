import math
def calcula_elongacao(a, phi, w, t):
    phi = math.radians(phi)
    wt = math.radians(w*t)
    elongacao = a*math.cos(phi)
    return elongacao