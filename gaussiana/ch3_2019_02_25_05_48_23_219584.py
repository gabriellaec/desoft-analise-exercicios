import math
def calcula_gaussiana(x, mi, sigma):
    f_x_mi_sigma = 1/(sigma*(2*math.pi)**(1/2))*math.e*-5*((x-mi)/sigma)**2
    print("O valor da gaussiana é {0}".format(f_x_mi_sigma))
x = float(input("Entre com o valor de x: "))
mi = float(input("Entre com o valor de mi: "))
sigma = float(input("Entre com o valor de sigma desejado: "))
calcula_gaussiana(x, mi, sigma)