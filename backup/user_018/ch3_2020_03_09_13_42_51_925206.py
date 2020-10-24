from math import e, sqrt, pi

def calcula_gaussiana(x, mi, sig):
    gauss = 1/(sqrt(2*pi)*sig)*e**(-0.5*(float((x-mi)/sig)**2)
    return gauss