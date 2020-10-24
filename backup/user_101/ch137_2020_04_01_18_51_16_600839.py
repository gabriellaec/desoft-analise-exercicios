from math import *

def calcula_aceleracao(r, f_rpm):
    f_hz = f_rpm / 60
    v_ang = 2 * pi * f_hz
    ac = (v_ang ** 2) * r
    return ac