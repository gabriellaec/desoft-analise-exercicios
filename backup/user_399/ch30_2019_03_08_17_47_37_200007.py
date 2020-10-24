import math
v=float(input("velocidade de lançamento: "))
O=float(input("ângulo de lançamento: "))
o=math.pi*O/180
def lanca_jaca(velocidade,angulo):
    g=9.8
    d=((velocidade**2)*math.sin(2*angulo))/g
    return d
a=lanca_jaca(v,o)
if a<=98:
    print("Muito perto")
elif a>=102:
    print("Muito longe")
else:
    print("Acertou!")