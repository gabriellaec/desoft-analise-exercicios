import math
def calcula_gaussiana(x, mi, sigma):
    primeira_parte=1/(sigma*((2*math.pi)**(1/2)))
    segunda_parte=math.exp(-0.5*((x-mi)/sigma)**2)
    final= primeira_parte*segunda_parte
    return final
