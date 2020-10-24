from math import *

for x in range(0,90):
    lista = []
    sen_x_formula = (4*x*(180-x))/(40500-x*(180-x))
    sen_x_automatico = sin(radians(x))
    lista.append(abs(sen_x_automatico) - abs(sen_x_formula))

print(max(lista))