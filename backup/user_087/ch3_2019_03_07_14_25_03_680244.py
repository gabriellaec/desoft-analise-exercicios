import math 
def calcula_gaussiana(x,μ,σ):
    f = math.exp((-0.5)*(((x - μ)/σ)**2))/(σ*((2*(math.pi)))**0.5)    
    return f

  

