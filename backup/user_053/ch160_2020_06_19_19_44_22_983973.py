import math

resultados = {}
valores = []
i = 0
for x in range(91):
    # Converte para rad
    x = x*math.pi/180
    # Aplica fórmula
    y = 4*x*(180 - x)/(40500 - x*(180 - x))
    # Verifica diferença
    dif = abs(y - math.sin(x))
    valores.append(dif)
    resultados[i] = dif
    i += 1

for indice, diferenca in resultados.items():
    if diferenca == max(valores):
        print(indice)
        break