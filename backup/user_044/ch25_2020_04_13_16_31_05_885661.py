import math
v=int(input("Qual a velocidade de lançamento de sua jaca? "))
ang=int(input("Qual o angulo de lancamento de sua jaca? "))
d=((v**2*(math.sin(math.radians(2*ang))))/9.8)
if d<90.00:
    print('Muito perto')
elif d==range(90.00,110.00):
    print('Acertou!')
elif d>110.00:
    print('Muito longe')