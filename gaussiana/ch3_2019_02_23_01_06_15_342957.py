#Importar a função math
import math

def calcula_gaussiana(x, μ, σ):
    y = (1/σ*(2*math.pi)**(1/2))*math.exp((-1/2)*((x-μ)/σ)**2);
    return y
x = 300 #Estou apenas supondo valores
μ = 30
σ = 1
d = calcula_gaussiana(x, μ, σ);
print(d);