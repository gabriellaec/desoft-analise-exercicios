import math
def f(x,mi,sigma):
    y=(1/(mi*(2*math.pi)**(1/2)))*math.exp(-0.5*(x-mi/sigma)**2)
    return y
