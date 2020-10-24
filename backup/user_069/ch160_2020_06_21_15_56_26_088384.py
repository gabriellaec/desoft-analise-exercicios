import math

dic_erros = {}

for x in range(0, 90):

    numerador = 4*x*(180-x)
    denominador = 40500 - x*(180-x)
    sin_bas = numerador/denominador 

    x_rad = math.radians(x)
    sin = math.sin(x_rad)

    erro = abs(sin_bas - sin)

    if not x in dic_erros:
        dic_erros[x] = erro

angulo_maior_erro = max(dic_erros, key = dic_erros.get)

print(angulo_maior_erro)