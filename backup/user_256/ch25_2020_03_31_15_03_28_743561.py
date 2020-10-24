import math
v=input("Qual a velocidade? ")
angulo=input("Qual o angulo? ")
    la = math.radians(angulo)
    d = ((v**2)*math.sin(la*2))/9,8
    if d<98:  
        print('Muito perto')
    if d>102:
        print('Muito longe')
    else:
        print('Acertou!')