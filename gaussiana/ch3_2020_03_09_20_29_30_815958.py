def calcula_gaussiana (x,sigma,mi):
    f=1/((sigma**1/2)*3.14)
    g=10**-0.5*((x-mi)/sigma)*2
    h=g*f
    return h