def calcula_gaussiana(x, mi, sigma):
    valor_gaussiana =  (1/(sigma*(sqrt(2*pi))))*((exp((-1)*(1/2)*(((x - mi)/sigma)**2))))
    return valor_gaussiana