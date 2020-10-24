from math import sin

erros_numero = {}

for number in range (0, 91):
    numero_sen = sin(number)
    est_bhask = (4*number*(180 - number))/(40500 - number*(180 - number))
    difference = numero_sen - est_bhask
    erros_numero[number] = abs(difference)
print(max(erros_numero, key=erros_numero.get))
