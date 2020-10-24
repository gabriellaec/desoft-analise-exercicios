def calcula_gaussiana(x, mi, sigma): 
    a = 1 / (sigma*(2*math.pi)**1/2)
    b = -1/2*((x-mi)/sigma)**2
    return a*e*b