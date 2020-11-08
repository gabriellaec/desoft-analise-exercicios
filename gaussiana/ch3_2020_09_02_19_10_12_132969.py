def calcula_gaussiana(a,b,c):
    resultado= math.exp(-0.5*((a-b)/c)**2)/(c*math.sqrt(2)*math.pi)
    return resultado