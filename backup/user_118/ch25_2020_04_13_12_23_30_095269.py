import math
velocidade=float(input('Diga a velocidade da jaca? '))
graus=float(input('Diga o ângulo em graus? '))
gravidade=9.8
distancia=(velocidade**2*(math.sin(math.radians(2*graus)))/gravidade
    if 98 <=distancia <=102:
        print ('Acertou!')
    elif distancia<98:
        print ('Muito perto')
    else:
        print ('Muito longe')
