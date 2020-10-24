import math

resultados = {}
valores = []
i = 0
for x in range(91):
    # Aplica fórmula
    y = 4*x*(180 - x)/(40500 - x*(180 - x))
    # Converte para rad
    x = x*math.pi/180
    # Verifica diferença
    dif = abs(y - math.sin(x))
    # Adiciona na lista de diferenças
    valores.append(dif)
    # Adiciona diferença com índice no dicionário
    resultados[i] = dif
    i += 1

for indice, diferenca in resultados.items():
    if diferenca == max(valores):
        print(indice)
        break