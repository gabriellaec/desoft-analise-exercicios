import math

g=9.8

v=int(input('velocidade:'))
teta=int(input('angulo:'))
      
def distancia_projetil(v,teta):
    teta=math.radians(2*teta)
    distancia=(v**2*math.sin(teta))/g
    if float(distancia)<98:
        resultado=str('Muito perto')
    elif 98<=float(distancia)<=102:
        resultado=str('Acertou!')
    else:
        resultado=str('Muito longe')
    return resultado

print(distancia_projetil(v,teta))
