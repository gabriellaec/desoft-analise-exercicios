import math
qual_velocidade = float(input('Qual a velocidade da jaca?'))
qual_angulo = float(input('Qual o angulo de lançamento em graus?'))

d = (qual_velocidade**2)*(math.sin(math.radians(2*qual_angulo)))/9.8
if d < 98:
    print ('Muito perto')
elif d > 102:
    print ('Muito longe')
else: 
    print ('Acertou!')