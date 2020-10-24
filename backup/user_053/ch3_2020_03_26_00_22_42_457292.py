# Importando funções matemáticas
import math
# Definindo a função
def calcula_gaussiana(x, mi, sigma):
    y=(1/sigma*(2*math.pi)**0.5)*math.e**(-0.5*((x-mi)/sigma)**2)
    return y

a=2
b=5
c=9
print(calcula_gaussiana(a,b,c))