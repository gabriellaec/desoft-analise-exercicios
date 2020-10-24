import math

def seno(x):
    numerador = 4 * x * (180 - x)
    denominador = 40500 - x * (180 - x)
    resultado = numerador / denominador
    return resultado

maior_erro = 0
graus_maior_erro = 0
for i in range(0,91):
    erro = seno(i) - math.sin(i)
    if abs(erro) > maior_erro:
        maior_erro = erro
        graus_maior_erro = i

print(graus_maior_erro)
