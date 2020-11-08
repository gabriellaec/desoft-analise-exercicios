def calcula_gaussiana(x,mi,sigma):
    den=sigma*(2*math.pi)**0,5
    pot=-0,5*((x-mi)/sigma)**2
    valor=(1/den)*math.exp(pot)
    return valor

    
    
    