import math
def lanca_jaca(velocidade,angulo):
    d=((velocidade**2)*math.sin(2*angulo))/g
    return d
g=9.8
v=float(input("velocidade de lançamento: ")
O=float(input("ângulo de lançamento: ")
a=lanca_jaca(v,O)
if a<98:
      print("Muito perto")
elif a>102:
      print("Muito longe")
else:
      print("Acertou!")