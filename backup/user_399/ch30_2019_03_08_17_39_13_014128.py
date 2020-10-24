import math
def lanca_jaca(velocidade,angulo):
    g=9.8
    d=((velocidade**2)*math.sin(2*angulo))/g
    return d
v=float(input("velocidade de lançamento: "))
O=float(input("ângulo de lançamento: "))
a=lanca_jaca(v,O)
if a<=98:
      print("Muito perto")
elif a>=102:
      print("Muito longe")
else:
      print("Acertou!")