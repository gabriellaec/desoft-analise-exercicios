import math
v = int(input('Qual a velocidade? '))
teta = int(input('Qual o angulo? '))
radiano = math.radians(teta)
g = 9.8

d = (v**2*math.sin(2*radiano))/g
           

if 100 - d < 2:
	print("Muito perto")
elif 100 - d == 0:
    print("Acertou!")
else:
    print("Muito longe")
