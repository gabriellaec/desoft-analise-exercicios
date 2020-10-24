import math
def tempo_de_vida_perdido(c,a):
    y = (10/1440)*c*(a*365)
    return y
c = int(input("Quantos cigarros fuma por dia?: ")
a = int(input("Fuma fazem quantos anos?: ")
d = tempo_de_vida_pedido(c,a)
   
print(d)