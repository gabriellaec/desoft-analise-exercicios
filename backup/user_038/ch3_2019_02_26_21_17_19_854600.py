import math
def calcula_gaussiana(x, mi, sigma):
    f_x_mi_sigma = 1/(sigma*(2*math.pi)**(1/2))*math.e*-5*((x-mi)/sigma)**2
    return f_x_mi_sigma