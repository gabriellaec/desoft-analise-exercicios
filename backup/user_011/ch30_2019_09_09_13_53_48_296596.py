import math
v = int(input('Qual a velocidade? '))
teta = int(input('Qual o angulo? '))
radiano = math.radians(teta)
g = 9.8

d = (v**2*math.sin(2*radiano))/g
           

if abs(100 - d) < 2:
	print("Acertou!")
elif d < 98:
    print("Muito perto")
else:
    print("Muito longe")
