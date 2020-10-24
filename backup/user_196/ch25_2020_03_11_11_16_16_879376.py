a = float (input("Qual a velocidade?"))
b = float (input("Qual o ângulo de lançamento?"))
g = 9.8
from math import sin
d = ((a**2)*(sin*(2*b)))/(g)
if d == 100 or d == 98 or d == 102:
    print ("Acertou!")
elif d < 98:
    print ("Muito perto")
else: 
    print ("Muito longe")
