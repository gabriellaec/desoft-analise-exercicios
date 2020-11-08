import math

def calcula_gaussiana(x, mi, sig):
    f=(1/(sig*(math.sqrt(2*(math.pi))))**(-(1/2)*(((x-mi)/sig)**2))
    return f
