import math

maiordiferenca = 0
angulo = 0

for a in range(91):
    seno_bhask = (4*a * (180 - a)) / (40500 - a*(180-a))
    seno_py = math.sin(math.radians(a))
    diferenca_seno = abs(seno_bhask - seno_py)
    if diferenca_seno > maiordiferenca:
        maiordiferenca = diferenca_seno
        angulo = a
        
print(angulo)