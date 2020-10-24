import math

lado= []
angulo= [] 
lado.append(0)
angulo.append(0)
def bhaskara(x):
    sin= (4*x*(180-x))/(40500-(x*(180-x)))
    return sin
for i in range(0, 91, 1):
    seno= math.sin(math.radians(i))
    resultado_seno= bhaskara(i)
    total= resultado_seno - seno
    if total > lado[0]:
        lado[0]= abs(total)
        angulo[0]= i
print(angulom[0])