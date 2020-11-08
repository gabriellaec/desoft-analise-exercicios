import math

def calcula_gaussiana(x, mi, sigma):

    if(sigma == 0):

        return(0)

    elif(mi == 0) and (x == 0):

        return(1)

    return((1 / (sigma * math.sqrt( math.pi * 2 ) ) ) ** ( (-0.5) *( (x-mi) / sigma)**2 ) )
