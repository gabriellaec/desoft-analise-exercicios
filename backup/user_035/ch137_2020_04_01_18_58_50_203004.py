import math
def calcula_aceleracao(r, f):
    fhz = (1/60)*f
    omega = 2*math.pi*fhz
    ac = (omega**2)*r
    return ac