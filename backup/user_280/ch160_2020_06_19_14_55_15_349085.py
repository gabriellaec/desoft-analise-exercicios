import math
erros = []

i = 0
while i < 90:
    erros.append(abs(4*x*(180-x)/(40500 - x*(180-x)) - math.sin(math.radians(x))))
    i+=1
    
print(max(erros))