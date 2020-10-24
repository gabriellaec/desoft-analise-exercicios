import math

def calcula_trabalho(f, thetaR, s):
    theta = float(thetaR) 
    theta = thetaR*(180/math.pi)
    t= f*math.cos(theta)*s
    tJ = float(t)
    return tJ
