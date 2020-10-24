from math import sin,radians
g=9.8
v=float(input("Qual a velocidade de lançamento: "))
angulo=float(input("Qual o ângulo de lançamento: "))
def d(v,angulo):
    d = (v**2*sin(radians(2*angulo)))/g
    if (d>102):
        return ("Muito longe")
    elif (d<=98):
        return ("Muito perto")
    else:
        return ("Acertou1")
print (d)