import math
def f(x,mi,sigma):
    return (1/(sigma*(2*math.pi)**1/2))*math.exp(-0.5((x-mi)/sigma)**2)