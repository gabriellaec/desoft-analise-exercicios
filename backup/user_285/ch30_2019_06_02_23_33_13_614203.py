import math
v=int(input("Velocidade: ")
θ=int(input("Angulo: ")
g=9.8
d= (v**2 * math.sin(2*θ))/g
if d<98:
    print("Muito perto")
elif d>98 and d<102:
    print ("Acertou!")
else:
    print("Muito longe")
