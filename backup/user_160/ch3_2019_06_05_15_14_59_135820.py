def calcula_gaussiana (x,mi,sigma):
    if x and mi and sigma > 0 and sigma != sqr(2*pi):
        gauss = (1/(sigma*sqr(2*pi)))*exp*(-0.5*(x-mi/sigma)**2)
        return gauss
        
    

    