import math
velocidade = float(input("Digite sua velocidade:"))
angulo = math.radians(float(input("Digite o ângulo de lançamento:")))
d = velocidade**2 * math.sin(2*angulo)/9.8
if d < 98:
    print ("Muito perto")
elif d > 102:
    print ("Muito longe") 
else:
    print ("Acertou!")