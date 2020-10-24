from math import e,sqrt,pi,radians  
def calcula_gaussiana (x,y,z):
    A=((-0.5)*(float(x-y)/z)**2)
    f= 1/((z*sqrt*(2*radians(pi)))*e**A)
    return f