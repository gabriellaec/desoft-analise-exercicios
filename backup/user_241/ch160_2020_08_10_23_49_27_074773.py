import math
grau = 0
erro = 0

for i in range(91):
    seni = (4 * i *(180 - i))/(40500 - i * (180 - x))
    diferença = math.abs(seni - math.sin(i)) 
    if diferença > erro:
        erro = diferença
        grau = i
print(grau)