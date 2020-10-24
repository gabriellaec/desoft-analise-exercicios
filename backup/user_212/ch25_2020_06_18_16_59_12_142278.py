import math

velo = float(input("Qual a velocidade de lançameto?"))
teta = float(input("Qual o ângulo de lançamento?"))

r=0

g = 9.8
teta_r = math.radians(2*teta)

d = ((velo**2)*math.sin(teta_r))/g


    
if d <= 102 or d>=98:
    r = 'Acertou!'

elif d <  98:
    r = 'Muito perto'
else :
    r = 'Muito longe'
print(r)