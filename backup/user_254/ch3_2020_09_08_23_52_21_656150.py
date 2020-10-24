# função que recebe 3 números reais e calcula gaussiana
import math
def calcula_gaussiana(x,μ,σ):
    w=σ*math.sqrt(2 * math.pi)
    y=1/w
    z=y*10**-0.5*((x-μ)/σ)**2
    return z
