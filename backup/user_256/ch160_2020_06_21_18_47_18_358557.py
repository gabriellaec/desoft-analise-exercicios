import math
erro = 0
angulo = 0
for x in range (91):
    seno = (4*x*(180 - x))/ (40500 - x*(180-x))
    formula = math.sin(math.radians(x))
    diferenca = abs(seno - formula)
    if diferenca > erro:
        erro = diferenca
        angulo = x
print(angulo)
        
        