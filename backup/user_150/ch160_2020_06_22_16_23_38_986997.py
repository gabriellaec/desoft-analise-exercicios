from math import sin, radians

dicDif = {}

for x in range(0, 91):
    senX = (4 * x * (180 - x)) / (40500 - x * (180 - x))
    senReal = sin(radians(x))
    dicDif[x] = abs(senReal - senX)

for x, dif in dicDif.items():
    maiorDif = max(dicDif, key=dicDif.get)

print(maiorDif)