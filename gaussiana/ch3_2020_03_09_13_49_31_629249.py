import math
def calcula_gaussiana(x,y,z):
    G =(1/z*math.sqrt(2*math.pi))*math.e**(-0.5*(x-y/z)**2)
    return G
x=1
y=1
z=1
print(calcula_gaussiana(x,y,z))