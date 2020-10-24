#S= S0 + V0*t + (a*(t**2))/2
#100*2= 0 + 0 + a*(t**2)
#t = (200/a)**1/2
#a = v

import math

def calcula_tempo(lista):
    dict= {}
    for k, v in lista.items():
        t = math.sqrt(200/v)
        dict[k] = t
    return dict
        