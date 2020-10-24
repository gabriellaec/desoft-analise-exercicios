import math
def x(v,teta,y0,g):
    q1=(v**2)/2*g
    q2=(1+(2*g*y0)/(v**2+math.sin(teta)**2))**0.5
    q3=(1+q2)*math.sin(20)
    d=q1*q3
    return d