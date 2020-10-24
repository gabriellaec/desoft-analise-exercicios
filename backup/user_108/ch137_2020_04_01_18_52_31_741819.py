import math
def calcula_aceleracao(raio,freq):
    v_ang = 2 * math.pi * freq/60
    return v_ang**2 * raio