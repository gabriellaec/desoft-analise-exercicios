import math
def calcula_gaussiana(x, mi, sigma):
    z = 1/(sigma*(2*math.pi)**(1/2))
    y = math.exp(-0.5*((x-mi)/sigma)**2)
    f_x_mi_sigma = z*y
    return f_x_mi_sigma