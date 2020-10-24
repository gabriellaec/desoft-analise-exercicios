import math
g = 9.8
veloc = int(input("Qual a velocidade da jaca?: "))
ang = int(input("Qual o ângulo de lançamento?: "))
d = ((veloc**2)*math.sin(2*ang))/g
if d >= 98 and d <= 102:
    print("Acertou!")
elif d < 98:
    print("Muito perto")
else:
    print("Muito longe")
    
 