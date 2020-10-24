#Programa que calcula a medida de catetos em um triangulo retângulo
import math
def encontra_cateto(c,h):
    x = ((h**2)-(c**2))**(1/2)
    return x
print(encontra_cateto(4,5))