import math
def alcance(v,theta,y0):
    a = v**2*math.sin(2*theta)/10
    return a
b = alcance(2,30,0)
print(b)
