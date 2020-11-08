import math
def calcula_gaussiana(x,μ,σ):
    parte1=1/(σ*(2*math.pi)**(1/2))
    parte2=math.exp(-0.5*((x-μ)/σ)**2)
    return (parte1*parte2)