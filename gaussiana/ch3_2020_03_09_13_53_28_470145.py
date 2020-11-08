def calcula_gaussiana(x,mi,sig):
    from math import pi
    calcula_gaussiana = (1/(sig*((2*pi)**(1/2))))**(-0.5 *(((x-mi)/sig)**2))
    return calcula_gaussiana
