def calcula_gaussiana ( x, mi, sigma):
    g = (1/ sigma * (2* pi)** 1/2)** (-1/2*(x-mi/sigma)**2)
    return g
