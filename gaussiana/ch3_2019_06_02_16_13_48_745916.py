import math
def calcula_gaussiana(x,μ,σ):
    gauss = (1/σ*math.sqrt(math.pi*2))**(-0.5*((x-μ)/σ)**2)
    if σ>0:
        return gauss
 