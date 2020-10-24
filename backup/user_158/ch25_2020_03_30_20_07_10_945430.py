import math
def catapulta(v,a):
    d=(v**2*math.sin(2*a))/9.8
    return d

V=int(input("velocidade de lancamento"))
A=int(input("angulo de lancamento"))

tentativa= catapulta(V,A)

if tentativa == 100:
    print('Acertou!')
elif tentativa < 100:
    print('Muito perto')
else:
    print('Muito longe')
