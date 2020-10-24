import math


def calcula_aceleracao (r,f):
    W = 0
    Pi = 0
    Ac = 0
    #converter RPM para frequencia
    # rpm/60 = x Hz
    Hz = f/60
    #Primeiro calcula velocidade angular(w)
    pi = math.pi
    w = 2*pi*Hz

    Ac = (w**2)*r

    return (Ac)