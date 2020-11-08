import math
def calcula_gaussiana(X, U, S):
    Tt=(1/(S*math.sqrt(2*math.pi)))*math.e**(-(1/2)*((X-U)/S)**2)
    return Tt
print (calcula_gaussiana(1, 2, 3))