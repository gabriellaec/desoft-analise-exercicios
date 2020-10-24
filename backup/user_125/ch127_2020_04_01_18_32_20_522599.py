import math
def calcula_elongacao (a,inicio,VelAng,tempo):
    x=a*math.cos(math.radians(inicio)+math.radians(VelAng)*tempo)
    return x
