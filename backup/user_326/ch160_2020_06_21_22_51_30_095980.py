from math import sin, radians

erros_numero = {}

for number in range (0, 91):
    numero_sen = sin(radians(number))
    est_bhask = (4*number*(180 - number))/(40500 - number*(180 - number))
    difference = est_bhask - numero_sen
    erros_numero[number] = abs(difference)
print(max(erros_numero, key=erros_numero.get))
