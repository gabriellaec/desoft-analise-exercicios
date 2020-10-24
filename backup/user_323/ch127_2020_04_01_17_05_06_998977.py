import math
def calcula_elongacao(O, A, T, W):
    x=A*math.cos(math.radians(O+W*T))
    return x