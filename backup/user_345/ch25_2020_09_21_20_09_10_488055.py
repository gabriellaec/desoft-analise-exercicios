import math
g = 9.8

angulo=int(input('Qual o angulo do lacamento? ')
vel=int(input('Qual a velocidade do lancamento? ')
             
def angulo_em_radianos(angulo):
    r = (graus * math.pi)/180
    return r

radianos = angulo_em_radianos(angulo)

def projetil_jaca(vel, radianos):
    d = ((vel**2) * math.sin(2*radianos))/g
    return d
                 
proximidade = projetil_jaca(vel, radianos)
                 
  if proximidade < 98:
     print ('Muito perto')
  elif proximidade > 102:
     print ('Muito longe')
  else:
     print ('Acertou!')