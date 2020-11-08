def calcula_gaussiana(x, mi, sigma):
    gauss = (1*exp(((-0,5)*(((x-mi)/sigma))**2)))/(sigma*sqrt(2*math.pi))
    return gauss
  