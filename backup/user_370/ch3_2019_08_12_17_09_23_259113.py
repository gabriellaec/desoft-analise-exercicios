import math 
def calcula_gaussiana (x,μ,σ):
    f=(1/σ*(2* math.pi)**(1/2))*math.exp(-0.5*((x-μ)/σ)**2)

