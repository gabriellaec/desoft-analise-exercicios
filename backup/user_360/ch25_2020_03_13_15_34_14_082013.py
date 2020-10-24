import math
v = int(input("Qual a velocidade do lançamento?"))
a = int(input("Qual o ângulo do lançamento?"))
g=9.8
d= ((v**2)* math.sin(2*math.radians(a))/g
	if d>102 :
    print("Muito longe")
	elif d>98:
    print("Muito perto")
	else:
    print("Acertou!")