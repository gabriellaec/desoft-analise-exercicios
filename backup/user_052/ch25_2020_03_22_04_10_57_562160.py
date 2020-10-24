import math
velocidade = int(input("Digite sua velocidade:\n"))
angulo = int(input("Digite o ângulo de lançamento:\n"))
d = velocidade**2 * math.sin(2*angulo)/9.8
if d < 98:
    print ("Muito perto")
elif d >= 98 and d <= 102:
    print ("Acertou!") 
else:
    print ("Muito longe")