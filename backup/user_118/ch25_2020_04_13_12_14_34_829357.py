import math
def jacawars(v,t,g):
    d=(v**2*(math.sin(2t))/g
    return d
velocidade=input('Diga a velocidade da jaca? ')
graus=input('Diga o ângulo em graus? ')
gravidade=9.8
distancia=jacawars(velocidade, graus, gravidade)
if 98<distancia<102:
    print ('Acertou!')
elif distancia<98:
    print ('Muito perto')
else:
    print ('Muito longe')
