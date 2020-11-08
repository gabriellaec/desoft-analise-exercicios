import math

def calcula_gaussiana(x, mi, sg):
    f = (1/(sg*((math.sqrt(2*math.pi)))))
    f1 = f * math.e**(-0.5*(((x-mi)/sg)**2))
    return f1