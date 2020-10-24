import math
def f(x,mi,sigma):
    y=(1/sigma*math.sqrt(2*math.pi))*math.e**(-0.5((x*mi)/sigma)**2))
    return y