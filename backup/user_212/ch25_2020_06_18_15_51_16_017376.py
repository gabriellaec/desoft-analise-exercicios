import math

velo = float(input("Qual a velocidade de lançameto?"))
teta = float(input("Qual o ângulo de lançamento?"))

r=0

g = 9.8
teta_r = radians(2*teta)

d = ((velo**2)*sin(teta_r))/g

if d > 100 :
    r = 'Muito longe'
    
if d == 100 or d>=(100-2):
    r = 'Acertou!'

elif d <98:
    r = 'Muito perto'
    
print(r)