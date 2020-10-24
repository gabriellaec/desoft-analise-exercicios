import math

v=int(input('qual a velocidade da sua jaca?'))
a=int(input('qual o angulo do lancamento da sua jaca?'))

def jacawars(v,a):
    d=v**2*(math.sin(2*a))/9.8
    if 98<=d<=102:
        return 'Acertou!'
    elif 90<=d<=110:
        return 'Muito perto'
    else:
        return 'Muito longe'
    
print(jacawars(v,a))
              