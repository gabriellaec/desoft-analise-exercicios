import math

def calcula_gaussiana(x,mi,sigma):
    part1 = 1/(sigma * (2 * math.pi) ** (1/2))
    part2 = part1 ** ((-1/2) * ((x - mi)/ sigma) ** (2))
    return(part2)