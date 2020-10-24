import math
erros = []

i = 0
while i < 90:
    erros.append(abs(4*i*(180-i)/(40500 - i*(180-i)) - math.sin(math.radians(i))))
    i+=1
    
print(max(erros))