from math import *

v = int(input("Qual a velocidade da sua jaca? "))
θ = int(input("Qual o angulo de lancamento? "))

d = int((v**2*sin(2*θ))/9.8)

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')
    
    
print(d)