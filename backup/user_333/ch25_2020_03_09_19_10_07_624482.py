import math

g=9.8

velocidade=float(input('velocidade:'))
angulo_teta=float(input('angulo:'))
      
def distancia_projetil(v,teta):
    teta_rad=math.radians(2*teta)
    distancia=(v**2*math.sin(teta_rad))/g
    if float(distancia)<98:
        resultado=str('Muito perto')
    elif 98<=float(distancia)<=102:
        resultado=str('Acertou!')
    else:
        resultado=str('Muito longe')
    return resultado

print(distancia_projetil(velocidade,angulo_teta))
