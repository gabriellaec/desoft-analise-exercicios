def calcula_gaussiana(x, y, z):
    pi= np.pi
    e= np.e
    w= 1/(z*(2*pi)**(1/2))*e**(-0.5*((x-y)/z)**2)
    return w

