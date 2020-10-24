import math
maior_dif = 0
grau = 0
for x in range(0,91):
    rad = math.radians(x)
    sen = (4*x*(180-x))/(40500-(x*(180-x)))
    sen_math = math.sin(rad)
    valor = abs(sen - sen_math)
    if valor > maior_dif:
        maior_dif = valor
        grau = x
print(grau)