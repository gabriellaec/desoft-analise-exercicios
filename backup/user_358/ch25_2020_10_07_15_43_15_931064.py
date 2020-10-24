import math
velocidade_da_jaca=int(input('qual a velocidade da jaca'))
angulo_de_lancamento=int(input('escolha o angulo'))

d_do_vizinho=100
g=9.8
seno_do_angulo_em_radianos=math.sin(math.radians(angulo_de_lancamento))
seno_do_angulo_em_graus=math.degrees(seno_do_angulo_em_radianos)
distancia_relativa=((velocidade_da_jaca**2)*(2*seno_do_angulo_em_graus))/g

if distancia_relativa>98 or <=102:
    print('Acertou!')
elif distancia_relativa>102:
    print('Muito longe')
else:
    print('Muito perto')

    
   