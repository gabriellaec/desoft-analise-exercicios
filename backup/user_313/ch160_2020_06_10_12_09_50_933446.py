import math
lista = list()
lista.append(0)
def calcula(x):
    sen = (4*x*(180-x))/(40500-(x*(180-x)))
    return sen

for i in range(0,91,1):
    sen_real = math.sin(math.radians(i))
    sen_calculado = calcula(i)
    
    if sen_calculado > sen_real:
        if sen_calculado > lista[0]:
            lista[0] = sen_calculado
    
print(lista[0])