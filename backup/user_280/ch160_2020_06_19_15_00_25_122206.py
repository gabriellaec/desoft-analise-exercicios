import math
erros = []

i = 0
while i < 90:
    erros.append(abs(4*i*(180-i)/(40500 - i*(180-i)) - math.sin(math.radians(i))))
    i+=1

i = 0
maximo = max(erros)
while i < 90:
    if erros[i] == maximo:
        print(i)
    else:
        i+=1
        