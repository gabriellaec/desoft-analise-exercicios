import math
def calcula_gaussiana(x,mi,sigma):
    a = sigma(**1/2*2*math.pi)
    b = math.exp
    c = -0,5*((x-mi)/sigma)**2
    t = 1/a*(b**c)
    return t
                                            