# função que recebe 3 números reais e calcula gaussiana
import math
def calcula_gaussiana(x,mi,sigma):
    w=sigma*math.sqrt(2 * math.pi)
    y=1/w
    z=y*10**-0.5*((x-mi)/sigma)**2
    return z