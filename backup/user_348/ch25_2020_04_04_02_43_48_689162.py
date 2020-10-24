import math
g = 9.8
v = float(input('valor da velocidade:'))
θ = float(input('valor do ângulo:'))
d = ((v**2)*math.sin(2*math.radians(θ)))/g
if d >= 98 and d<= 102:
    print("'Acertou!'")
elif d < 98:
    print("'Muito perto'")
else:
    print("'Muito longe'")