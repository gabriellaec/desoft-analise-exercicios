import math
vel = int(input("Qual a velocidade do lançamento?"))
ang = int(input("Qual o ângulo do lançamento?"))
g=9.8
d= ((vel**2)* math.radians(2*ang))/g
	if d==100 or d<102 or d>98:
        print("Acertou!")
	elif d<98:
        print("Muito perto")
    else:
        print("Muito Longe")

    