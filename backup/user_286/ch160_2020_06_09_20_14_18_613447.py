import math

lista_dif_erros = []

def sin_bhaskara(x):
    sinx = 4 * x * (180-x) / (40500 - x * (180 - x))
    return sinx

def sin_real(x):
    return math.sin(x)

for i in range(0,91):
    dif = math.fabs(sin_bhaskara(i) - sin_real(i))
    lista_dif_erros.append(dif)

print(lista_dif_erros.index(max(lista_dif_erros)))