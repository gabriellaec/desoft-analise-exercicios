import math
maior_diferenca = 0
x = 0
for x in range(91):
    senox=(4*x*(180-x))/(40500-x*(180-x))
    seno_n=math.sin(math.radians(x))
    diferenca=abs(senox-seno_n)
    if diferenca>maior_diferenca:
        maior_diferenca=diferenca
        angulo=x
print(angulo)
