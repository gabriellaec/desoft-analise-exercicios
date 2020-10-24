import math
v=int(input("Insira a velocidade da jaca "))
tetha=int(input("Insira o ângulo de lançamento "))
d=int(((v**2)*math.sin(2*tetha))/9.8)
if d<98:
    print('Muito perto')
elif 98<=d<=102:
    print('Acertou!')
elif d>102
    print('Muito longe')
    