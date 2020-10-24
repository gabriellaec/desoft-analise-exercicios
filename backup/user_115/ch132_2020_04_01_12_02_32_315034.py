import math

def calcula_trabalho(f, thetaD, s):
    thetaR = float(thetaD) 
    thetaR = thetaD/(180/math.pi)
    t= f*(math.cos(thetaR))*s
    tJ = float(t)
    return tJ
