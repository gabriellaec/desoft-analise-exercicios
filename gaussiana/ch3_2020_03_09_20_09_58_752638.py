def calcula_gaussiana(x, mi, sigma):
    a =(1/(sigma*((2*math.pi)**0.5)))
	b=(math.e)**(-0.5*(((x-mi)/sigma)**2))
    c=a*b
    return c