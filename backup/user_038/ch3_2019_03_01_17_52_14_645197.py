import math
def calcula_gaussiana(x, mi, sigma):
    x = 1/(sigma*(2*math.pi)**(1/2))
    y = math.e**(-0.5*((x-mi)/sigma)**2)
    f_x_mi_sigma = x*y
    return f_x_mi_sigma