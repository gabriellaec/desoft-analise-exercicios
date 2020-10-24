import math

def calcula_trabalho(f, thetaR, s):
    thetaD = float(thetaR) 
    thetaD = thetaR*(180/math.pi)
    t= f*(math.cos(thetaD))*s
    tJ = float(t)
    return tJ
