import math

def calcula_trabalho(f, thetaR, s):
    theta = float(thetaR) 
    theta = thetaR*(180/math.pi)
    t = float(t)
    t= f*math.cos(theta)*s
    return t

f = 0,5
thetaR = 20
s = 10

print(calcula_trabalho(f, thetaR, s))