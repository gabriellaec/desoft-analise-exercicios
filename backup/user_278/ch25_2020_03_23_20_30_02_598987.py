import math

a= ângulo desejado
d= distância 

d=(v**2)*math.sin(2*a)/9.8
         if d<98:
         	return "Muito perto"
         elif 98<=d<=102:
         	return "Muito longe"
         else:
         	return "Acertou!"