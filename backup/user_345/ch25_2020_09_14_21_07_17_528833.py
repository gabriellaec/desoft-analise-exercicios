import math
g = 9.8

def angulo_em_radianos(graus):
    r = (graus * math.pi)/180
    return r

def projetil_jaca(v,r):
    d = ((v**2) * math.sin(2*r))/g
    return d

angulo = int(input('Qual o angulo do lacamento? ')
x = angulo_em_radianos(angulo)

velocidade = int(input('Qual a velocidade do lancamento? ')

a = projetil_jaca(velocidade,x)
  if a < 98:
     print ('Muito perto')
  elif a > 102:
     print ('Muito longe')
  else:
     print ('Acertou!')