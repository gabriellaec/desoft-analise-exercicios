import math

def calcula_gaussiana(x,w,z):
    y = 1/z*(2*math.pi)**(1/2)
    t = math.e**(-0,5*((x-w)/z)**2)
    p = y*t
    return p

# w= mi
# z= sigma
