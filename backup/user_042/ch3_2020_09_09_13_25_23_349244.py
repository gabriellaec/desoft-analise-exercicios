def f(x,u,s):
    y= 1/(s * (2*math.pi)**(1/2))*math.e**(-0.5*((x-u)/s)**2)
    return y