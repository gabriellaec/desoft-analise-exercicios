import math
def catapulta(v,a):
    d=(v**2*math.sin(2*a))/9.8
    return d

V=input("velocidade de lancamento")
A=input("angulo de lancamento")

tentativa= catapulta(V,A)

if tentaiva == 100:
    print('Acertou!')
elif tentativa < 100:
    print('Muito perto')
else:
    print('Muito longe')
