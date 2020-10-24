from math import sin, radians 
velocidade= float(input('Digite a velocidade de sua jaca '))
angulo= float(input('Digite o angulo de lancamento de sua jaca ')) 
def distancia_jaca(velocidade,angulo): 
  g=9.8
  d=(velocidade**2)*sin(2*(radians(angulo)))/g
  if d==2:
	  return('Acertou!') 
  elif d>2:
    return('Muito longe') 
  else:
    return('Muito perto')