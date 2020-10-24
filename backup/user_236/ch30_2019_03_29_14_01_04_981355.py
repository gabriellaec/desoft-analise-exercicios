import math
def lancamento (v,teta):
    d=v**2*math.sin(2*teta)/9.8
    return d
V=float(input("qual a velocidade? "))
T=float(input("qual angulo"))
D= lancamento(V,T)
if D<98:
    print("Muito perto")
elif D>102:
    print("Muito longe")
else:
    print ("Acertou!")