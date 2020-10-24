from math import sin, radians
jacas= float(input("qual a velocidade de lançamento de sua jaca: "))
jacas2= float(input("qual o ângulo de lançamento da sua jaca: "))
d= (jacas**2*sin*(radians(2*jacas2)))/9.8
if d>=98 and d<=102:
    print("Acertou!")
elif d<98:
    print("Muito perto")
else:
    print("Muito longe") 

