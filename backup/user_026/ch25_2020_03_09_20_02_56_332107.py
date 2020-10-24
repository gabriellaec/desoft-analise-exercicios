from math import sin, radians
veloci= float(input("diga a velocidade de lançamento da sua jaca: "))
angulo= float(input("diga o angulo da sua jaca (em graus): "))
d= ((veloci**2)*sin*radians(2*angulo)/9.8)
if d<98 and d<= 102:
    print("Acertou!")
elif d<=98:
    print ("Muito perto")
elif d>=102:
    print ("Muito longe")

