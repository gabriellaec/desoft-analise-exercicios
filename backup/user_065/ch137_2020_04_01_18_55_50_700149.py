import math
def calcula_aceleracao(r, f):
    f = f/60
    omega = 2*math.pi*f
    accelCentrip = (omega**2) * r
    return accelCentrip