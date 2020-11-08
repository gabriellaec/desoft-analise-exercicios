sigma = input('Digite um número: ')
x =input('Digite um número: ')
mi = input('Digite um número: ')

def calcula_gaussiana(sigma, pi, e, x, mi):
    calcula_gaussiana = (((1/(sigma*((2*pi)**(1/2)))*e)(-0.5*((x-mi)/sigma)**2))
    return calcula_gaussiana