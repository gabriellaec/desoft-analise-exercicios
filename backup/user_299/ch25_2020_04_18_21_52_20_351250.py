import math

velo = float(input('digite a velocidade da jaca:'))
ang = float(input('digite o angolo de disparo:'))
ang_rad = math.radians(ang)
def distancia_percorrida(v , teta):
    g = 9.8
    d = v*v*math.sin(2*teta)/g
    return d
d = distancia_percorrida(velo,ang_rad)
daoq = d*d
if daoq < 9604:
    print('Muito perto')
elif daoq <= 10404:
    print('Acertou!')
else:
    print('Muito longe')

