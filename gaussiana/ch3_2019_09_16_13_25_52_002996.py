from math import e, sqrt, pi

def calcula_gaussiana(x,mi,sigma):
    divisao = 1/(sigma*sqrt(2*pi))
    exp = ((-0.5)*(((x-mi)/sigma)**2))
    y = e**exp
    gauss = divisao*y
    return gauss