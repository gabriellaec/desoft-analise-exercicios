import math
def calcula_gaussiana(x,μ,σ):
    gauss = (1/σ*math.sqrt(math.pi*2))**(-0.5*((x-μ)/σ)**2)
    if x!=0 or μ!=0 and σ>0:
        return gauss
 