import math

def calcula_gaussiana(a,b,c):
    p1=(1/(c*math.pow((2*math.pi),(1/2))))
    p2=((-0.5)*((a-b)/c)**2)
    r=p1*math.exp(p2)
    return r 

   
 