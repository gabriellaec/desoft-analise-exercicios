def calcula_gaussiana(x,u,sigma):
    e= -0.5 * ((x-u)/sigma)**2
    f = (1/sigma * (2*3.14)**1/2)**e
    return f