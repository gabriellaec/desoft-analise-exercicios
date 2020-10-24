import math
g = 9.8

angulo = int(input('Qual o angulo do lacamento? ')
velocidade = int(input('Qual a velocidade do lancamento? ')
             
def angulo_em_radianos(angulo):
    r = (graus * math.pi)/180
    return r

radianos = angulo_em_radianos(angulo)

def projetil_jaca(velocidade, radianos):
    d = ((velocidade**2) * math.sin(2*radianos))/g
    return d
                 
proximidade = projetil_jaca(velocidade, radianos)
                 
  if proximidade < 98:
     print ('Muito perto')
  elif proximidade > 102:
     print ('Muito longe')
  else:
     print ('Acertou!')