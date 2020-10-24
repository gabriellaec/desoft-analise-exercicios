import math
v = int(input('Qual a velocidade? '))
teta = int(input('Qual o angulo? '))
radiano = math.radians(teta)
g = 9.8

d = (v**2*math.sin(2*radiano))/g
           
d_espalhada = d + math.pi*2**2

if 100 - d_espalhada < 2:
	print("Muito pertp")
elif 100 - d_espalhada == 0:
    print("Acertou!")
else:
    print("Muito longe")
